from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API = 'YOUR_BOT_TOKEN'
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

calculate_button = KeyboardButton(text='Рассчитать')
kb = ReplyKeyboardMarkup(resize_keyboard=True).add(calculate_button)

calories_button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
formulas_button = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
main_menu_kb = InlineKeyboardMarkup().add(calories_button, formulas_button)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет. Это простой бот расчета калорий!', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def option(message):
    await message.answer('Выберите опцию', reply_markup=main_menu_kb)


@dp.callback_query_handler(text='formulas')
async def inform(call):
    await call.message.answer('10 x вес(кг) + 6,25 x рост(см) - 5 x возраст(г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state: FSMContext):
    await state.update_data(user_age=message.text)
    await message.answer('Введите свой рост в сантиметрах:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state: FSMContext):
    await state.update_data(user_growth=message.text)
    await message.answer('Введите свой вес в килограммах:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state: FSMContext):
    await state.update_data(user_weight=message.text)
    data = await state.get_data()
    try:
        weight = float(data["user_weight"])
        growth = float(data["user_growth"])
        age = int(data["user_age"])
        calories = 10 * weight + 6.25 * growth - 5 * age + 5
        await message.answer(f'Количество калорий вашего тела: {calories:.2f}')
    except ValueError:
        await message.answer("Ошибка ввода данных. Убедитесь, что вы вводите числа.")
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
