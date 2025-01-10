from fastapi import FastAPI
from fastapi.routing import APIRouter
from routers.task import router as task_router
from routers.user import router as user_router

app = FastAPI()


@app.get('/')
def root():
    return {"message": "Welcome to Taskmanager"}


# Подключение маршрутов
app.include_router(task_router, prefix="/task", tags=["task"])
app.include_router(user_router, prefix="/user", tags=["user"])
