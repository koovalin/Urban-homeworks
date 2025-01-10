from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI()

# User list and model
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users", response_model=List[User])
def get_users():
    return users


@app.post("/user/{username}/{age}", response_model=User)
def add_user(
    username: Annotated[
        str,
        Path(
            title="Enter username",
            description="Имя пользователя, строка длиной от 5 до 20 символов",
            min_length=5,
            max_length=20,
            example="UrbanUser",
        ),
    ],
    age: Annotated[
        int,
        Path(
            title="Enter age",
            description="Возраст пользователя, целое число от 18 до 120",
            ge=18,
            le=120,
            example=24,
        ),
    ],
):
    new_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}", response_model=User)
def update_user(
    user_id: Annotated[
        int,
        Path(
            title="Enter User ID",
            description="ID пользователя, существующий ключ в списке users",
            example=1,
        ),
    ],
    username: Annotated[
        str,
        Path(
            title="Enter username",
            description="Имя пользователя, строка длиной от 2 до 20 символов",
            min_length=2,
            max_length=20,
            example="UrbanProfi",
        ),
    ],
    age: Annotated[
        int,
        Path(
            title="Enter age",
            description="Возраст пользователя, целое число от 18 до 120",
            ge=18,
            le=120,
            example=28,
        ),
    ],
):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}", response_model=User)
def delete_user(
    user_id: Annotated[
        int,
        Path(
            title="Enter User ID",
            description="ID пользователя, существующий ключ в списке users",
            example=2,
        ),
    ]
):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
