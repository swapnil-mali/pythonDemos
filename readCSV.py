#!/usr/bin/python3


import csv

file = open("input.csv", 'r')

header = []
rows = []

csvReader = csv.reader(file)

header = next(csvReader)

print(header)

for row in csvReader:
    rows.append(row)

print(rows)
