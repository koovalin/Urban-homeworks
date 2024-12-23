from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import crud_functions

API = '7757947891:AAHAK5FKxIL4mdW-SMN-cxEHefs78K0l2lk'
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

simple_calculate_button = KeyboardButton(text='Рассчитать')
simple_buy_button = KeyboardButton(text='Купить')
start_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(simple_calculate_button, simple_buy_button)

calories_button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
formulas_button = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
main_menu_kb = InlineKeyboardMarkup().add(calories_button, formulas_button)

product_1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
product_2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
product_3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
product_4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
product_5 = InlineKeyboardButton(text='Product5', callback_data='product_buying')
product_6 = InlineKeyboardButton(text='Product6', callback_data='product_buying')
product_7 = InlineKeyboardButton(text='Product7', callback_data='product_buying')
product_8 = InlineKeyboardButton(text='Product8', callback_data='product_buying')
back_to_catalog = InlineKeyboardButton(text='Back', callback_data='back_to_catalog')

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [product_1, product_2],
        [product_3, product_4],
        [product_5, product_6],
        [product_7, product_8]
    ]
)


# product_buying_kb = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text='Buy', url='https://www.ya.ru'), back_to_catalog]
#     ])


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Привет {message.from_user.username}.\nЭто простой бот расчета калорий!',
                         reply_markup=start_kb)


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


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = crud_functions.get_all_products()
    for product in products:
        with open(f'img/{product[1]}.jpg', 'rb') as img:
            await message.answer_photo(img, f'Название: {product[1]} | Описание: {product[2]} | Цена:{product[3]}')
    await message.answer('Выберите продукт для покупки:', reply_markup=catalog_kb)


@dp.callback_query_handler(text='back_to_catalog')
async def back_to_catalog(call):
    await call.message.answer('Выберите продукт для покупки.', reply_markup=catalog_kb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')


@dp.message_handler()
async def all_messages(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')
    await message.reply('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
