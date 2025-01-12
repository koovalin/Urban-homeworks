from fastapi import FastAPI
from backend.db import Base, engine
from models import *

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to Taskmanager"}


Base.metadata.create_all(bind=engine)

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))
print(CreateTable(Task.__table__))