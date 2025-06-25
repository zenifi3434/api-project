# FastAPI Task Manager API

A simple REST API built with FastAPI and Pydantic to manage tasks. Supports create, read, update, and delete (CRUD) operations.

## Features

- Create tasks with title, description, and completion status
- Update existing tasks partially
- List all tasks or get a specific task by ID
- Delete tasks
- Simple in-memory storage for demonstration

## How to Run

1. Install dependencies: pip install fastapi uvicorn pydantic

2. Run the app: uvicorn main:app --reload

3. Open your browser at http://127.0.0.1:8000/docs for the interactive API docs.


