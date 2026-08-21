employees = [
    {"name": "Ankit", "salary": 50000, "experience": 3},
    {"name": "Owaish", "salary": 65000, "experience": 5},
    {"name": "Vishal", "salary": 70000, "experience": 2},
    {"name": "Rohit", "salary": 45000, "experience": 6},
    {"name": "Aman", "salary": 80000, "experience": 4}
]

for employee in employees:
    print(employee["name"])

for employee in employees:
    if employee["salary"] >= 60000:
        print(employee["name"])

highly_experienced = []
for employee in employees:
    if employee["experience"] >= 5:
        highly_experienced.append(employee)
print(highly_experienced)

for employee in employees:
    if employee["salary"] < 50000:
        employee["salary"] += 5000
        print(employee)

