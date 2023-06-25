from taskmanager import TaskManager
from task import Task


def test_task_is_added():
    task_manager = TaskManager()
    assert task_manager.get_number_of_tasks() == 0

    new_task = Task("new task")
    task_manager.add_task(new_task)
    assert task_manager.get_number_of_tasks() == 1

