import pytest

from task import Task


@pytest.fixture
def simple_task():
    return Task("new task")

def test_print_task(simple_task):
    assert simple_task.task_title == "new task"
    assert simple_task.status == "Not done"

def test_update_title(simple_task):
    simple_task.task_title = "changed task"
    assert simple_task.task_title == "changed task"
    assert simple_task.status == "Not done"

def test_update_status_to_done(simple_task):
    simple_task.change_status()
    assert simple_task.task_title == "new task"
    assert simple_task.status == "Done"

def test_update_status_to_not_done(simple_task):
    simple_task.change_status()
    simple_task.change_status()
    assert simple_task.task_title == "new task"
    assert simple_task.status == "Not done"