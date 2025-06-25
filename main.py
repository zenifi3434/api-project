from fastapi import FastAPI, Depends
from typing import Optional
from pydantic import BaseModel

# Define the Task model with title, optional description, and completion status
class Task(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool

# Model for updating a task - all fields optional since you might update only some
class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

app = FastAPI()

# Simple in-memory storage for tasks
tasks = {}

# Dependency to get the task storage
def get_tasks():
    return tasks

# Create a new task with an ID
@app.post("/create-task/{task_id}")
def create_task(task_id: int, task: Task):
    if task_id in tasks:
        return {"error": "Task with this ID already exists"}
    tasks[task_id] = task
    return task

# Get all tasks
@app.get("/get-all-tasks")
def get_all_tasks(db = Depends(get_tasks)):
    return db

# Get a task by ID
@app.get("/get-task/{task_id}")
def get_task(task_id: int, db = Depends(get_tasks)):
    if task_id not in db:
        return {"error": "Task not found"}
    return db[task_id]

# Update task details by ID
@app.put("/update-task/{task_id}")
def update_task(task_id: int, task_update: UpdateTask):
    if task_id not in tasks:
        return {"error": "Task not found"}

    existing_task = tasks[task_id]

    # Update only the fields provided in the request
    if task_update.title is not None:
        existing_task.title = task_update.title
    if task_update.description is not None:
        existing_task.description = task_update.description
    if task_update.completed is not None:
        existing_task.completed = task_update.completed

    return existing_task

# Delete a task by ID
@app.delete("/delete-task/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        return {"error": "Task not found"}
    del tasks[task_id]
    return {"success": "Task deleted"}
