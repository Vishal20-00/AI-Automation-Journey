employees = [
    {"name": "Vishal", "salary": 32000},
    {"name": "Rinku", "salary": 90000},
    {"name": "Rashmi", "salary": 60000},
    {"name": "Amit", "salary": 100000}

]

for employee in employees:
    print(employee["name"], employee["salary"])
    if employee["salary"]  >= 60000:
        print(employee["name"], "qualified")

print(len(employees))