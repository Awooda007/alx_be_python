# daily_reminder.py

# Prompt the user for task description, priority, and time-sensitivity
task = input("Enter the task for today: ")
priority = input("Enter the priority of the task (high, medium, low): ").lower()
time_bound = input("Is the task time-sensitive? (yes/no): ").lower()

# Process the task based on priority using Match Case
match priority:
    case "high":
        priority_message = "This task is of high priority."
    case "medium":
        priority_message = "This task is of medium priority."
    case "low":
        priority_message = "This task is of low priority."
    case _:
        priority_message = "Invalid priority level. Please choose from high, medium, or low."

# Modify the reminder if the task is time-sensitive
if time_bound == "yes":
    time_message = "This task requires immediate attention today!"
else:
    time_message = "This task can be completed later."

# Provide the customized reminder
print(f"Reminder: {task}. {priority_message} {time_message}")
