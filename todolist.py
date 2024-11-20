def add_task(tasks):
    # Adds a task to the list
    task = input("Enter a task: ")
    tasks.append(task)
    print( f" '{task}' Task added successfully!")

def view_tasks(tasks):
        # Displays the list of tasks
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def remove_task(tasks):
    # Removes a task from the list
    view_tasks(tasks)
    task_index = int(input("Enter the number of the task to remove: ")) - 1
    if task_index >= 0 and task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f" '{removed_task}' Task removed successfully!")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True: 
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()