import time
from plyer import notification
import threading

tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")

def notify_task(task):
    notification_title = "Task Reminder"
    notification_message = f"It's time to do your task: {task}"
    notification.notify(
        title=notification_title,
        message=notification_message,
        timeout=10
    )

def set_reminder():
    if len(tasks) == 0:
        print("No tasks found!")
        return
    print("Select a task to set a reminder for:")

    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

    choice = int(input("Enter task number: "))
    if choice < 1 or choice > len(tasks):
        print("Invalid choice!")
        return

    task = tasks[choice - 1]
    time_remaining = input("Enter time remaining in minutes: ")

    try:
        time_remaining = int(time_remaining)
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    if time_remaining <= 0:
        print("Invalid input! Time remaining should be a positive number.")
        return

    time_diff = time_remaining * 60

    reminder_thread = threading.Timer(time_diff, notify_task, args=(task,))
    reminder_thread.start() 

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found!")
        return

    print("Tasks for today:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")



while True:

    print("1. Add a task")
    print("2. Set a reminder")
    print("3. View tasks")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_task()
    elif choice == 2:
        set_reminder()
    elif choice == 3:
        view_tasks()
    elif choice == 4:
        break
    else:
        print("Invalid choice!")

    input("\nPress Enter to continue...")