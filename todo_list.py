import json
import os

FILE_NAME = "todo_list.json"

def load_task() :
    if os.path.exists(FILE_NAME) :
        with open(FILE_NAME , "r") as file :
            return json.load(file)

    return []

def save_tasks(tasks) :
    with open(FILE_NAME , "w") as file:
        json.dump(tasks , file , indent= 4)

def add_task(tasks_list, task_name):
    new_task = {
        "name" : task_name , 
        "status" : "pending"
    }
    tasks_list.append(new_task)
    save_tasks(tasks_list)

def delete_task(tasks_list , index ) :
    if 0 <= index < len(tasks_list) :
        tasks_list.pop(index)
        save_tasks(tasks_list)

def complete_task(tasks_list , index) :
    if 0 <= index < len(tasks_list) :
        tasks_list[index]["status"] = "Done"
        save_tasks(tasks_list)

