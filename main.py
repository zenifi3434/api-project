import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hi():
    return{"Hello":"From Docke"}