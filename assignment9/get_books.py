import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')  # Optional, recommended for Windows
options.add_argument('--window-size=1920x1080')  # Optional, set window size
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")


data=[]

results = driver.find_elements(By.CSS_SELECTOR, 'li.cp-search-result-item')
print (f"Number of results: {len(results)}")
for item in results:
    title,author,year="N/A"
    try:
        title_element = item.find_element(By.CSS_SELECTOR, 'span.title-content').text.strip()
        title = title_element
    except Exception as e:
        print (f"Error: {e}")

    authors = item.find_elements(By.CSS_SELECTOR, 'a.author-link')
    if authors:
        authors_list = [author.text.strip() for author in authors if author.text.strip()]
        author="; ".join(authors_list)
    else:
        print("Author not found for ")


    try:
        format_year_div = item.find_element(By.CSS_SELECTOR, 'div.cp-format-info')
        format_year_span = format_year_div.find_element(By.CSS_SELECTOR, 'span.display-info-primary')
        year = format_year_span.text.strip()
    except Exception as e:
        print (f"Error: {e}")

    data.append({"Title":title, "Author":author,"Format-Year":year})
driver.quit()
print(data)

results_df =  pd.DataFrame(data)
print(results_df)
results_df.to_csv('./get_books.csv', index=False)


with open('./get_books.json', 'w') as f:
    json.dump(data, f, indent=4)
