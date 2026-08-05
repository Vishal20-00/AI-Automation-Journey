def salary_report(salary):
    return salary * 0.10

names = ["Ankit", "Owaish", "Vishal", "Shubham"]
salaries = [50000,60000, 70000, 80000]
for name in names:
 for salary in salaries:
    print("Employee:", name), print("Salary:", salary), print("Bonus:", salary_report(salary))
