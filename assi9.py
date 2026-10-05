import csv
import json

f = open("input.csv", "r")

data = csv.DictReader(f)

rows = []

for row in data:
    rows.append(row)

f.close()

f = open("output.json", "w")

json.dump(rows, f, indent=4)

f.close()

print("CSV data converted to JSON")
