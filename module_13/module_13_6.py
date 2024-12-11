from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API = 'YOUR_API_TOKEN'
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

button1 = InlineKeyboardButton(text='Рассчитать', callback_data='Рассчитать')
button2 = InlineKeyboardButton(text='Инфо', callback_data='Info')
kb = InlineKeyboardMarkup(resize_keyboard=True).add(button1, button2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет. Это простой бот расчета калорий!', reply_markup=kb)


@dp.callback_query_handler(text='Info')
async def inform(call):
    await call.message.answer('Это простой бот расчета калорий!', reply_markup=kb)
    await call.answer()


@dp.callback_query_handler(text='Рассчитать')
async def set_age(call):
    await call.message.answer('Введите свой возраст')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state: FSMContext):
    await state.update_data(user_age=message.text)
    await message.answer('Введите свой рост в сантиметрах')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state: FSMContext):
    await state.update_data(user_growth=message.text)
    await message.answer('Введите свой вес в килограммах')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state: FSMContext):
    await state.update_data(user_weight=message.text)
    data = await state.get_data()
    weight = float(data["user_weight"])
    growth = float(data["user_growth"])
    age = int(data["user_age"])
    calories = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f'Количество калорий вашего тела: {calories:.2f}')
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
