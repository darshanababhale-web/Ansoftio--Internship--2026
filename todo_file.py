import json

try:
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
except:
    tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Save & Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        for i, t in enumerate(tasks):
            print(i+1, t)

    elif choice == "3":
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)
        print("Saved!")
        break
