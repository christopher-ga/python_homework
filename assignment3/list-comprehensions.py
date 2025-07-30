import csv

with open("../csv/employees.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

full_names = [f"{row[1]} {row[2]}" for row in data[1:]]
print("All names:", full_names)

names_with_e = [name for name in full_names if "e" in name]
print("Names with 'e':", names_with_e)
