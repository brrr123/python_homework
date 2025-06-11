import pandas as pd

df = pd.read_csv("../csv/employees.csv")

employee_names = [f"{row[1]['first_name']} {row[1]['last_name']}" for row in df.iterrows()]
print("List of employee names:")
print(employee_names)


names_with_e = [name for name in employee_names if "e" in name.lower()]
print("\nList of names containing the letter 'e':")
print(names_with_e)