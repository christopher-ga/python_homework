import pandas as pd

# task 1

dictionary = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(dictionary)

# task 2

task2_employees = pd.read_csv('dirty_data.csv')
json_employees = pd.read_json('additional_employees.json')
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)