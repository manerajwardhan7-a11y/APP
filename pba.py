import json
import csv

with open("students.json", "r") as file:
    data = json.load(file)

with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print("JSON converted to CSV successfully!")
