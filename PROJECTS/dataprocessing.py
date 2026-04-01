import csv
employees = [
    {"id": 1, "name": "Arun", "role": "Designer", "salary": 35000},
    {"id": 2, "name": "Meena", "role": "Developer", "salary": 45000},
    {"id": 3, "name": "Kumar", "role": "Manager", "salary": 60000}
]
print("Original Data:", employees)
with open("employees.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "role", "salary"])
    writer.writeheader()
    writer.writerows(employees)

print("Data stored in employees.csv")
with open("employees.csv", newline='') as f:
    reader = csv.DictReader(f)
    employees_from_csv = list(reader)
print("Reloaded from CSV:", employees_from_csv)
