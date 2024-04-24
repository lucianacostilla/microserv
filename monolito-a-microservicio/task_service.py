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

