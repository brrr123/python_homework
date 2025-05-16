import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')  # Optional, recommended for Windows
options.add_argument('--window-size=1920x1080')  # Optional, set window size
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get("https://owasp.org/www-project-top-ten/")


data=[]
ul_element = driver.find_element(By.XPATH, "/html/body/main/div/div[1]/section[1]/ul[2]")

li_elements = ul_element.find_elements(By.TAG_NAME, "li")

for li in li_elements[:10]:
    a_tag = li.find_element(By.TAG_NAME, "a")
    title = a_tag.text.strip()
    href = a_tag.get_attribute("href")
    data.append({"title": title, "link": href})

results_df =  pd.DataFrame(data)
print(results_df)
results_df.to_csv('./owasp_top_10.csv', index=False)




driver.quit()