#1
employees = [
{"name": "Vishal", "salary": 300000 },
{"name": "Rashmi", "salary": 500000},
{"name": "Shubham", "salary": 10000000},
{"name": "Neeraj", "salary": 10000000000000000},
{"name": "Rakhi", "salary": 5000000000000000000000}
]

for employee in employees:
    print(employee["name"], employee["salary"])



#2
employee = {"name": "Rahul", "age": 28, "salary": 55000, "department": "sales"}
employee["salary"] = 60000
employee["experiance"] = 5

for key in employee: #if we don't know the keys 
    print(key,employee[key])

#3
employees = [
    {"name": "Ankit", "salary": 50000},
    {"name": "Owaish", "salary": 60000},
    {"name": "Vishal", "salary": 70000},
    {"name": "Rohit", "salary": 45000}
]

for employee in employees:
    if employee["salary"] >= 60000:
        print(employee["name"], "qualifies")