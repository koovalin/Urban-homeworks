from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup



API = 'YOUR_BOT_TOKEN'
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Calories')
async def set_age(message):
    await message.answer('Введите свой возраст')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(user_age=message.text)
    data = await state.get_data()
    await message.answer(f'Ваш возраст - {data["user_age"]}')
    await message.answer('Введите свой рост в сантиметрах')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_growth(message, state):
    await state.update_data(user_growth=message.text)
    data = await state.get_data()
    await message.answer(f'Ваш рост - {data["user_growth"]} см')
    await message.answer('Введите свой вес в килограммах')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_weight(message, state):
    await state.update_data(user_weight=message.text)
    data = await state.get_data()
    await message.answer(f'Ваш вес - {data["user_weight"]} кг')
    calories = float(10 * float(data["user_weight"]) + 6.25 * int(data["user_growth"]) - 5 * int(data["user_age"]) + 5)
    await message.answer(f'Количество калорий вашего тела: {calories}')

    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
