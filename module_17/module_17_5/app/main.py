from fastapi import FastAPI
from backend.db import Base, engine
from routers.user import router as user_router
from routers.task import router as task_router

# Инициализация приложения
app = FastAPI()

# Подключение маршрутов
app.include_router(user_router)
app.include_router(task_router)


# Главный маршрут
@app.get("/")
def root():
    return {"message": "Welcome to Taskmanager"}


# Создание таблиц в БД
Base.metadata.create_all(bind=engine)
