from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from models import Task, User
from schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify
from backend.db_depends import get_db

router = APIRouter(
    prefix="/task",
    tags=["task"]
)


# Получение всех задач
@router.get("/")
def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


# Получение по ID
@router.get("/{task_id}")
def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=404, detail="Task was not found")
    return task


# Создание
@router.post("/create")
def create_task(task: CreateTask, user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    slug = slugify(task.title)
    stmt = insert(Task).values(
        title=task.title,
        content=task.content,
        priority=task.priority,
        user_id=user_id,
        slug=slug
    )
    db.execute(stmt)
    db.commit()
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


# Обновление
@router.put("/update/{task_id}")
def update_task(task_id: int, task: UpdateTask, db: Annotated[Session, Depends(get_db)]):
    stmt = update(Task).where(Task.id == task_id).values(
        title=task.title,
        content=task.content,
        priority=task.priority
    )
    result = db.execute(stmt)
    db.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task was not found")
    return {"status_code": status.HTTP_200_OK, "transaction": "Task update is successful!"}


# Удаление
@router.delete("/delete/{task_id}")
def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    stmt = delete(Task).where(Task.id == task_id)
    result = db.execute(stmt)
    db.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task was not found")
    return {"status_code": status.HTTP_200_OK, "transaction": "Task deletion is successful!"}
