# module_14_5.py
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import crud_functions

API = 'YOUR_API_KEY'
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

simple_calculate_button = KeyboardButton(text='Рассчитать')
simple_buy_button = KeyboardButton(text='Купить')
register_button = KeyboardButton(text='Регистрация')
start_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(simple_calculate_button, simple_buy_button, register_button)

calories_button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
formulas_button = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
main_menu_kb = InlineKeyboardMarkup().add(calories_button, formulas_button)


# Inline кнопки для магазина
catalog_kb = InlineKeyboardMarkup()
back_to_catalog_button = InlineKeyboardButton(text='Назад в каталог', callback_data='back_to_catalog')


def create_catalog_buttons():
    products = crud_functions.get_all_products()
    for product in products:
        catalog_kb.add(InlineKeyboardButton(text=product[1], callback_data='product_buying'))
    catalog_kb.add(back_to_catalog_button)


create_catalog_buttons()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Привет {message.from_user.username}. Это простой бот расчета калорий!',
                         reply_markup=start_kb)


@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state: FSMContext):
    if crud_functions.is_included(message.text):
        await message.answer("Пользователь существует, введите другое имя:")
    else:
        await state.update_data(username=message.text)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state: FSMContext):
    try:
        age = int(message.text)
        if age <= 0:
            raise ValueError
        await state.update_data(age=age)
        data = await state.get_data()
        crud_functions.add_user(data['username'], data['email'], data['age'])
        await message.answer("Регистрация прошла успешно!")
        await state.finish()
    except ValueError:
        await message.answer("Возраст должен быть положительным числом. Попробуйте снова:")


@dp.callback_query_handler(lambda call: call.data.startswith('buy_'))
async def buy_product(call):
    product_id = int(call.data.split('_')[1])
    product = crud_functions.get_product_by_id(product_id)
    if product:
        await call.message.answer(f"Вы купили {product}! Спасибо за покупку!")
    else:
        await call.message.answer("Произошла ошибка. Попробуйте снова.")


@dp.message_handler(text='Рассчитать')
async def option(message):
    await message.answer('Выберите опцию', reply_markup=main_menu_kb)


@dp.callback_query_handler(text='formulas')
async def inform(call):
    await call.message.answer('10 x вес(кг) + 6,25 x рост(см) - 5 x возраст(г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age_to_calc(call):
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


@dp.callback_query_handler(text='back_to_catalog')
async def back_to_catalog(call):
    await call.message.answer("Вы вернулись в каталог.", reply_markup=catalog_kb)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = crud_functions.get_all_products()
    for product in products:
        with open(f'img/{product[1]}.jpg', 'rb') as img:
            await message.answer_photo(img, f'Название: {product[1]} | Описание: {product[2]} | Цена:{product[3]}')
    await message.answer('Выберите продукт для покупки:', reply_markup=catalog_kb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')


@dp.message_handler()
async def all_messages(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')
    await message.reply('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
