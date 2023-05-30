import pickle

class Task:
    def __init__(self, name, description, due_date, completed=False):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.completed = completed
    
    def mark_complete(self):
        self.completed = True
    
    def __str__(self):
        status = "Completed" if self.completed else "Incomplete"
        return f"Name: {self.name}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {status}\n"
    
class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.mark_complete()
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for task in self.tasks:
                print(task)
    def save_tasks(self):
        with open("tasks.pickle", "wb") as file:
            pickle.dump(self.tasks, file)

    def load_tasks(self):
        try:
            with open("tasks.pickle", "rb") as file:
                self.tasks = pickle.load(file)
        except FileNotFoundError:
            self.tasks = []

def show_menu():
    print("\nTo-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task Complete")
    print("4. Save Tasks")

def main():
    todo_list = ToDoList()
    todo_list.load_tasks()

    while True:
        show_list = ToDoList()
        show_list.load_tasks()

        while True:
            show_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                todo_list.view_tasks()
            elif choice == "2":
                name = input("Enter task name: ")
                description = input("Enter task description: ")
                due_date = input("Enter task due date: ")
                task = Task(name, description, due_date)
                todo_list.add_task(task)
                print("Task added successfully.")
            elif choice == "3":
                task_name = input("Enter task name: ")
                todo_list.mark_task_complete(task_name)
                print("Task marked complete successfully.")
            elif choice == "4":
                todo_list.save_tasks()
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()