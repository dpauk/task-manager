class TaskManager():
    """Implement a TaskManager class that acts as a container for tasks.
    It should provide methods to add, update, delete, and filter tasks,
    as well as manage the persistence of task data."""
    
    def __init__(self):
        self.task_list = []
    
    def add_task(self, task):
        self.task_list.append(task)

    def get_number_of_tasks(self):
        return len(self.task_list)
    
    def print_all_tasks(self):
        for task in self.task_list:
            print(task.print_task())

    pass