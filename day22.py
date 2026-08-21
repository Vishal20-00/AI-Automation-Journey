students = [
    {"name": "Vishal", "marks": 461},
    {"name": "Rinku", "marks": 500},
    {"name": "Manish", "marks": 350},
    {"name": "Neeraj", "marks": 800},
    {"name": "Mukul", "marks": 250},
    {"name": "Ramdev", "marks": 431}
]

for student in students:
    if student["marks"] >= 500:
        print(student["name"], student["marks"], "Qualified for the interview")

qualified_candidates = []
for student in students:
    if student["marks"] >= 500:
        qualified_candidates.append(student)
print(qualified_candidates)

for student in students:
    if student["marks"] < 500:
        student["marks"] += 100
        print(student["name"], student["marks"])