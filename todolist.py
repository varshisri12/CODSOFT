import os

# A class to represent the to-do list
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task['completed'] else "Not Completed"
                print(f"{i + 1}. {task['task']} - {status}")

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' removed.")
        else:
            print("Invalid task number.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    to_do_list = ToDoList()
    
    while True:
        clear_screen()
        print("To-Do List:")
        to_do_list.view_tasks()
        
        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            to_do_list.add_task(task)
        elif choice == '2':
            task_number = int(input("Enter the task number to mark as completed: "))
            to_do_list.mark_task_completed(task_number)
        elif choice == '3':
            task_number = int(input("Enter the task number to remove: "))
            to_do_list.remove_task(task_number)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
