"""A Python program for adding, completing, and removing tasks"""
# List to store tasks
tasks = []

# Function to display tasks
def display_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks):
            status = "Done" if task[1] else "Not Done"
            print(f"{index + 1}. {task[0]} ({status})")
# Function to add a task
def add_task(description):
    tasks.append([description, False])
    print(f"Task '{description}' added to your to-do list.")
# Function to mark a task as completed
def mark_task_completed(task_number):
    if 0 <= task_number < len(tasks):
        tasks[task_number][1] = True
        print(f"Task {task_number + 1} marked as completed.")
    else:
        print("Invalid task number.")
# Function to remove a task
def remove_task(task_number):
    if 0 <= task_number < len(tasks):
        removed_task = tasks.pop(task_number)
        print(f"Task '{removed_task[0]}' removed from your to-do list.")
    else:
        print("Invalid task number.")
# Main function to run the task manager
def main():
    while True:
        print("\nOptions:")
        print("1. Display to-do list")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_tasks()
        elif choice == '2':
            description = input("Enter the task: ")
            add_task(description)
        elif choice == '3':
            display_tasks()
            task_number = int(input("Enter the task number to mark as completed: ")) - 1
            mark_task_completed(task_number)
        elif choice == '4':
            display_tasks()
            task_number = int(input("Enter the task number to remove: ")) - 1
            remove_task(task_number)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if _name_ == "_main_":
    main()