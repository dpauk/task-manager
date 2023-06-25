class Task():
    """Create a Task class to represent individual tasks.
    It should encapsulate the task properties, such as name, due date, and status,
    and provide methods for updating and retrieving task information."""
    
    def __init__(self, task_title):
        self._task_title = task_title
        self._status = "Not done"
    
    @property
    def task_title(self):
        """The title of the task"""
        return self._task_title
    
    @task_title.setter
    def task_title(self, new_title):
        self._task_title = new_title

    @property
    def status(self):
        """Either 'Done' or 'Not done"""
        return self._status
    
    def change_status(self):
        if self._status == "Done":
            self._status = "Not done"
        else:
            self._status = "Done"
    
    pass