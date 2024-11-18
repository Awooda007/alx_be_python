# daily_reminder.py

# Prompt the user for task description, priority, and time-sensitivity
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority using Match Case
match priority:
    case "high":
        priority_message = "high priority task"
    case "medium":
        priority_message = "medium priority task"
    case "low":
        priority_message = "low priority task"
    case _:
        priority_message = "invalid priority level. Please enter high, medium, or low."

# Modify the reminder based on time-sensitivity
if time_bound == "yes":
    time_message = "that requires immediate attention today!"
else:
    time_message = "Consider completing it when you have free time."

# Provide the customized reminder
print(f"Reminder: '{task}' is a {priority_message} {time_message}")
