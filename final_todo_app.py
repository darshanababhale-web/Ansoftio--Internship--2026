import json

# Load tasks from file
try:
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
except:
    tasks = []

# Function to display tasks
def view_tasks():
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            status = "✔" if task["done"] else "✘"
            print(f"{i+1}. {task['task']} [{status}]")

while True:
    print("\n===== TO-DO APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Complete")
    print("5. Save & Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter task: ")
        tasks.append({"task": task_name, "done": False})
        print("Task added!")

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        view_tasks()
        try:
            num = int(input("Enter task number to delete: "))
            if 0 < num <= len(tasks):
                tasks.pop(num-1)
                print("Task deleted!")
            else:
                print("Invalid number!")
        except:
            print("Please enter valid number!")

    elif choice == "4":
        view_tasks()
        try:
            num = int(input("Enter task number to mark complete: "))
            if 0 < num <= len(tasks):
                tasks[num-1]["done"] = True
                print("Task marked as complete!")
            else:
                print("Invalid number!")
        except:
            print("Enter valid number!")

    elif choice == "5":
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)
        print("Tasks saved successfully!")
        break

    else:
        print("Invalid choice! Try again.")
