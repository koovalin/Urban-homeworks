from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {"1": "Имя: Example, возраст: 18"}


@app.get("/users")
def get_users():
    return users


@app.post("/user/{username}/{age}")
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
    new_id = str(max(map(int, users.keys())) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
def update_user(
    user_id: Annotated[
        str,
        Path(
            title="Enter User ID",
            description="ID пользователя, существующий ключ в словаре users",
            example="1",
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
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"User {user_id} has been updated"
    return {"error": f"User ID {user_id} not found"}


@app.delete("/user/{user_id}")
def delete_user(
    user_id: Annotated[
        str,
        Path(
            title="Enter User ID",
            description="ID пользователя, существующий ключ в словаре users",
            example="2",
        ),
    ]
):
    if user_id in users:
        del users[user_id]
        return f"User {user_id} has been deleted"
    return {"error": f"User ID {user_id} not found"}
