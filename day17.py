def bonus(salary):
    return salary * 0.10

employees = ["Rashmi", "Shubham", "Neeraj", "Manjeet", "Rakhi", "Vishal"]
salaries = [234563, 55554, 563214, 81555,222512, 888545]
for i in range(6):
    print([i], employees[i], salaries[i], bonus(salaries[i]))     