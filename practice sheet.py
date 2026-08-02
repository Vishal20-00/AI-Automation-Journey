def check_task(task_name, status):
    if status == "done":
        print(task_name, "completed.")
    else:
        print(task_name, "is pending.")

tasks = ["Python Study", "Git hub practice", "VS Code Practice"]
for task in tasks:
    status = input(f" {task} (done/ not done):").lower()
    check_task(task, status)

print("Daily Ai automation practice completed!")
