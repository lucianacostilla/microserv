class TaskViewer:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def list_tasks(self):
        for task in self.task_manager.tasks:
            print(f"Title: {task.title}, Description: {task.description}, Completed: {task.completed}")

