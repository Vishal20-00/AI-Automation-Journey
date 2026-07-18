enter_a_task = "yes"
task = input("Have you done Python Learning? (yes/no)").lower()
while task != enter_a_task:
    print("Done the task first")
    task = input("Have you done the task now? (yes/no)").lower()
print("Congratulations on completing the task!")