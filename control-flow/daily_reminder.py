task = input("Enter the task for today: ")
priority = input("Enter the priority of the task (high, medium, low): ").lower()
time_bound = input("Is the task time-sensitive? (yes/no): ").lower()
match priority:
    case "high":
        priority_message = "This task is of high priority."
    case "medium":
        priority_message = "This task is of medium priority."
    case "low":
        priority_message = "This task is of low priority."
    case _:
        priority_message = "Invalid priority level. Please choose from high, medium, or low."
if time_bound == "yes":
    time_message = "This task requires immediate attention today!"
else:
    time_message = "This task can be completed later."
print(f"Reminder: {task}. {priority_message} {time_message}")
