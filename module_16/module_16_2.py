from fastapi import FastAPI, Path
from typing import Annotated

# Создаем объект приложения FastAPI
app = FastAPI()


# Маршрут для главной страницы
@app.get("/")
def read_root():
    return {"message": "Главная страница"}


# Маршрут для страницы администратора
@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}


# Маршрут для страницы пользователя с ID
@app.get("/user/{user_id}")
def read_user_by_id(
    user_id: Annotated[
        int,
        Path(
            title="Enter User ID",
            description="ID пользователя, целое число от 1 до 100",
            ge=1,
            le=100,
            example=1,
        ),
    ]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


# Маршрут для передачи username и age
@app.get("/user/{username}/{age}")
def read_user_info(
    username: Annotated[
        str,
        Path(
            title="Enter username",
            description="Имя пользователя, строка длиной от 2 до 20 символов",
            min_length=2,
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
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
