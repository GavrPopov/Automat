import pytest
from Lesson_8_1.Pages import Task

zadacha = Task()

def test_todo():
    list = zadacha.get_list()
    assert list.status_code == 200
    params = {"title": "Python", "completed": 'false'}
    task = zadacha.create(params)
    assert task is not None
    
    params = {"title": "Python - Automat"}
    renamed_task = zadacha.rename(task, params)
    assert renamed_task.json()['title'] == "Python - Automat"
    info = zadacha.info(task)
    assert info.json()['title'] == "Python - Automat"
    assert info.json()['id'] == task

    params = {"completed": 'true'}
    satus_true = zadacha.change_status(task, params)
    assert satus_true == True

    params = {"completed": 'false'}
    satus_false = zadacha.change_status(task, params)
    assert satus_false == False

    deleting = zadacha.delete(task)
    assert deleting == 204