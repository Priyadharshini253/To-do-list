def display_menu():
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print(f"'{task}' has been added to your list.")

def update_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_num = int(input("\nEnter the task number to update: "))
        if 1 <= task_num <= len(tasks):
            updated_task = input("Enter the updated task: ")
            tasks[task_num - 1] = updated_task
            print(f"Task {task_num} has been updated.")
        else:
            print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"'{removed_task}' has been removed from your list.")
        else:
            print("Invalid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1-5.")

if __name__ == "__main__":
    main()
