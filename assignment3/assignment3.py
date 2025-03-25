import pandas as pd

#Task 1
##Subtask 1.1
task1_data_frame = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York',  'Los Angeles', 'Chicago']
})
print(task1_data_frame.head(3))

##Subtask 1.2
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary.head(3))

##Subtask 1.3
task1_older = task1_with_salary.copy()
task1_older['Age']+=1
print(task1_older.head(3))

##Subtask 1.4
task1_older.to_csv('./employees.csv', index=False)


#Task 2
##Subtask 2.1
task2_employees = pd.read_csv('./employees.csv')
print("task2_employees\n",task2_employees.head(3))

##Subtask 2.2
json_employees = pd.read_json('./additional_employees.json')
print("json_employees\n",json_employees.head(3))

##Subtask 2.3
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("more_employees\n",more_employees.head(5))

#Task 3
##Subtask 3.1
first_three = more_employees.head(3)
print("first_three\n",first_three)

##Subtask 3.2
last_two = more_employees.tail(2)
print("last_two\n",last_two)

##Subtask 3.3
employee_shape = more_employees.shape
print("employee_shape\n",employee_shape)

##Subtask 3.4
print (more_employees.info())

#Task 4
##Subtask 4.1
dirty_data=pd.read_csv('./dirty_data.csv')
print("dirty_data\n",dirty_data.head(3))
clean_data=dirty_data.copy()

##Subtask 4.2
clean_data=clean_data.drop_duplicates()
print("clean_data\n",clean_data.head(3))

##Subtask 4.3 and 4.5
clean_data['Age']=pd.to_numeric(clean_data['Age'], errors='coerce')
clean_data['Age']=clean_data['Age'].fillna(clean_data['Age'].mean())
print(clean_data['Age'])

##Subtask 4.4 and 4.5
clean_data['Salary']=pd.to_numeric(clean_data['Salary'], errors='coerce')
clean_data['Salary']=clean_data['Salary'].fillna(clean_data['Salary'].median())
print(clean_data['Salary'])

##Subtask 4.6
clean_data['Hire Date']=pd.to_datetime(clean_data['Hire Date'], errors='coerce')
print(clean_data['Hire Date'])

##Subtask 4.7
clean_data['Name']=clean_data['Name'].str.strip().str.upper()
clean_data['Department']=clean_data['Department'].str.strip().str.upper()
print(clean_data[['Name','Department']])