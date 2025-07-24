import csv
import traceback
import os
import custom_module
from datetime import datetime


# task 2

def read_employees():
    data = {}
    rows = []

    try:
        with open('../csv/employees.csv', newline='') as file:
            reader = csv.reader(file)

            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows.append(row)

        data["rows"] = rows
        return data

    except Exception as e:
        print("An exception occurred:", type(e).__name__)
        traceback.print_exc()
        exit(1)


employees = read_employees()
print(employees)


# task 3

def column_index(column_name):
    return employees["fields"].index(column_name)


# task 4
def first_name(row_number):
    index = column_index("first_name")
    return employees["rows"][row_number][index]


employee_id_column = column_index("employee_id")


# task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches


# task 5
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches


# task 7
def sort_by_last_name():
    last_name_index = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_index])
    return employees["rows"]


sort_by_last_name()
print(employees)


# task 8
def employee_dict(row):
    field_names = employees["fields"]
    result = dict(zip(field_names, row))
    result.pop("employee_id", None)
    return result


example_row = employees["rows"][0]
print(employee_dict(example_row))


# task 9
def all_employees_dict():
    emp_dict = {}
    id_index = column_index("employee_id")
    for row in employees["rows"]:
        emp_id = row[id_index]
        emp_dict[emp_id] = employee_dict(row)
    return emp_dict


print(all_employees_dict())


# task 10
def get_this_value():
    return os.getenv("THISVALUE")


# task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)


set_that_secret("abracadabra")
print("custom_module.secret:", custom_module.secret)


# task 12
def read_csv_as_dict(filepath):
    data = {}
    rows = []
    try:
        with open(filepath, newline='') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows.append(tuple(row))
            data["rows"] = rows
            return data
    except Exception as e:
        print(f"Error reading {filepath}: {type(e).__name__}")
        traceback.print_exc()
        exit(1)


def read_minutes():
    minutes1 = read_csv_as_dict('../csv/minutes1.csv')
    minutes2 = read_csv_as_dict('../csv/minutes2.csv')
    return minutes1, minutes2


minutes1, minutes2 = read_minutes()
print("Minutes1:", minutes1)
print("Minutes2:", minutes2)


# task 13
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)


minutes_set = create_minutes_set()
print("Combined Minutes Set:", minutes_set)


# task 14
def create_minutes_list():
    return list(map(lambda tup: (tup[0], datetime.strptime(tup[1], "%B %d, %Y")), minutes_set))


minutes_list = create_minutes_list()
print("Minutes list with datetime objects:", minutes_list)


# task 15
def write_sorted_list():
    sorted_list = sorted(minutes_set, key=lambda tup: datetime.strptime(tup[1], "%B %d, %Y"))

    converted_list = list(
        map(lambda tup: (tup[0], datetime.strptime(tup[1], "%B %d, %Y").strftime("%B %d, %Y")), sorted_list))

    try:
        with open("./minutes.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(minutes1["fields"])
            writer.writerows(converted_list)
    except Exception as e:
        print(f"Error writing file: {type(e).__name__}")
        traceback.print_exc()
        exit(1)

    return converted_list


final_minutes_list = write_sorted_list()
print("Sorted and written minutes list:", final_minutes_list)
