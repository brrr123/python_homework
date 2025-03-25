import traceback
import os
import custom_module
from datetime import datetime

#Task 2
import csv

def read_employees():
    headers = {}
    rows = []
    row_number = 0
    try:
        with open('../csv/employees.csv','r') as csvfile:
            employees_csv = csv.reader(csvfile)
            for row in employees_csv:
                if row_number == 0:
                    headers = row
                else:
                    rows.append(row)
                row_number += 1
            return {"fields": headers, "rows": rows}
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
employees = read_employees()
print (employees)


#Task 3
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

#Task 4
def first_name(row_number):
    return employees["rows"][row_number][column_index("first_name")]

#Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches

#Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

#Task 7
def sort_by_last_name():
    employees["rows"].sort(key=lambda row: row[column_index("last_name")])
    return employees["rows"]

print (sort_by_last_name())

#Task 8
def employee_dict(row):
    employee={}
    employee = dict(zip(employees["fields"], row))
    del employee["employee_id"]
    return employee

print (employee_dict(employees["rows"][0]))

#Task 9
def all_employees_dict():
    employees_dict = {}
    for row in employees["rows"]:
        employee_id = row[column_index("employee_id")]
        employees_dict[employee_id] = employee_dict(row)
    return employees_dict

print (all_employees_dict())

#Task 10
def get_this_value():
    return os.getenv("THISVALUE")

#Task 11
def set_that_secret(secret_value):
    custom_module.set_secret(secret_value)

set_that_secret("blah")
print (custom_module.secret)

#Task 12
def read_csv(filename):
    headers = {}
    rows = []
    row_number = 0
    try:
        with open(filename,'r') as csvfile:
            csv_file = csv.reader(csvfile)
            for row in csv_file:
                if row_number == 0:
                    headers = row
                else:
                    rows.append(tuple(row))
                row_number += 1
            return {"fields": headers, "rows": rows}
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

def read_minutes():
    return read_csv('../csv/minutes1.csv'), read_csv('../csv/minutes2.csv')


minutes1, minutes2 = read_minutes()
print (minutes1)
print (minutes2)

#Task 13
def create_minutes_set():
    m1= set(minutes1["rows"])
    m2= set(minutes2["rows"])
    return m1.union(m2)

minutes_set = create_minutes_set()
print (minutes_set)

#Task 14
def create_minutes_list():
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")) ,minutes_set))


minutes_list = create_minutes_list()
print (minutes_list)

#Task 15
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    sorted_minutes= list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    with open('./minutes.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(minutes1["fields"])
        for row in sorted_minutes:
            csvwriter.writerow(row)
    return sorted_minutes

print(write_sorted_list())