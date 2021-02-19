'''write generator which read from file employees data line by line:

Anna|20|devops|3
Vasya|50|pm|30'''

import csv


def csv_reader(file):
    for row in open(file, "r"):
        yield row

my_generator = csv_reader("EmployeesData.csv")

print(next(my_generator))
print(next(my_generator))
print(next(my_generator))


