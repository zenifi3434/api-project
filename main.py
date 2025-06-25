#Task Manager API
#Create Update Read DELETE Task
#Task has id,title,desc,completed
#Dependcy injection to manage a list
#Add a dependcy to simulate current user info
#Return proper response models with Pyndanctic validation


import fastapi
from fastapi import FastAPI,Depends
from typing import Optional
from pydantic import BaseModel

class Task(BaseModel):
    title : str
    description : Optional[str] = None
    completed : bool

class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


app = FastAPI()

all_tasks = {}

@app.post("/create-task/{id}")          #create
def create_task(id: int,task: Task):
    if id in all_tasks:
        return {"Error": "Already have a task assigned with this ID"}
    all_tasks[id] = task
    return task

@app.get("/get-all-tasks")          #read
def get_task():
    return all_tasks

@app.get("/get-task/{id}")          #read
def get_task(id:int):
    return all_tasks[id]

@app.put("/update-task/{id}")
def update_task(id:int, task : UpdateTask):
    if id not in all_tasks:
        return {"Error:":"A task has not been assigned to this ID"}
    if task.title is not None:
        all_tasks[id].title = task.title
    if task.description is not None:
        all_tasks[id].description = task.description
    if task.completed is not None:
        all_tasks[id].completed = task.completed



@app.delete("/delete-task")
def delete_task(id:int):
    if id not in all_tasks:
        return {"Error:":"A task has not been assigned to this ID"}
    del all_tasks[id]
    return{"Success":"Task Deleted"}