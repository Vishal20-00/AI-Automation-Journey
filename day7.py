task = "done"
task_1 = input("Have you completed the study of Python? (done/not done):").lower()
while task_1 != task:
    print("You haven't done your task Sir, Do your task first and if done write done")
    task_1 = input("Have you completed the study of Python? (done/not done):").lower()
print("Congratulation on completion of task 1")
task_2 = input("Have you done running? (done/not done):").lower()
while task_2 != task:
    print("You haven't done your task Sir, Do your task first and if done write done")
    task_2 = input("Have you done running? (done/not done):").lower()
print("Congratulation on completion of second task")
task_3 = input("Have you done reading books?: (done/not done)")
while task_3 != task:
    print("You haven't completed your task, do your task first")
    task_3 = input("Have you done your third task?: (done/not done)").lower()
print("Congratulations on the completion of third task.")