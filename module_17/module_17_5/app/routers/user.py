from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from models import User, Task
from schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify
from backend.db_depends import get_db

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


# Получение всех пользователей
@router.get("/")
def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users


# Получение пользователя по ID
@router.get("/{user_id}")
def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return user


# Создание пользователя
@router.post("/create")
def create_user(user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    slug = slugify(user.username)
    stmt = insert(User).values(
        username=user.username,
        firstname=user.firstname,
        lastname=user.lastname,
        age=user.age,
        slug=slug
    )
    db.execute(stmt)
    db.commit()
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


# Обновление пользователя
@router.put("/update/{user_id}")
def update_user(user_id: int, user: UpdateUser, db: Annotated[Session, Depends(get_db)]):
    stmt = update(User).where(User.id == user_id).values(
        firstname=user.firstname,
        lastname=user.lastname,
        age=user.age
    )
    result = db.execute(stmt)
    db.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="User was not found")
    return {"status_code": status.HTTP_200_OK, "transaction": "User update is successful!"}


# Удаление пользователя
@router.delete("/delete/{user_id}")
def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    stmt = delete(User).where(User.id == user_id)
    result = db.execute(stmt)
    db.commit()
    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="User was not found")
    return {"status_code": status.HTTP_200_OK, "transaction": "User deletion is successful!"}


# Получение всех задач пользователя
@router.get("/{user_id}/tasks")
def tasks_by_user_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    tasks = db.scalars(select(Task).where(Task.user_id == user_id)).all()
    return tasks


# Обновление функции удаления пользователя
@router.delete("/delete/{user_id}")
def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    # Удаление связанных задач
    db.execute(delete(Task).where(Task.user_id == user_id))

    # Удаление пользователя
    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User and related tasks deleted successfully!"}
