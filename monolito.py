class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        self.tasks.append(Task(title, description))

    def complete_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.completed = True
                break

    def list_tasks(self):
        for task in self.tasks:
            print(f"Title: {task.title}, Description: {task.description}, Completed: {task.completed}")

if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        print("1. Add Task")
        print("2. Complete Task")
        print("3. List Tasks")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)
        elif choice == "2":
            title = input("Enter task title to mark as completed: ")
            task_manager.complete_task(title)
        elif choice == "3":
            task_manager.list_tasks()
        else:
            break

