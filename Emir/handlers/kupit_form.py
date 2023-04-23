from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from db.base import create_clients


async def kupit_command(cb: types.CallbackQuery):
    '''
    Функция для того, чтобы пользователь купил авто
    '''
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text='Для того чтобы купить авто заполните форму /form2'
    )


class Form2(StatesGroup):
    product_id = State()
    name2 = State()
    phone_number2 = State()
    done = State()


async def cancel_handler2(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply('Выход из формы')


async def form_start2(cb: types.CallbackQuery, state: FSMContext):
    await Form2.product_id.set()

    async with state.proxy() as data:
        data['product_id'] = int(cb.data.replace('form_start2', ''))
    await Form2.next()
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text='Введите ваше имя:')

async def name_process2(message: types.Message, state: FSMContext):
    if not message.text.isalpha():
        await message.reply('Вводите только буквы!')
    else:
        async with state.proxy() as data:
            data['name2'] = message.text

        await Form2.next()
        await message.reply('Введите номер телефона:')


async def phone_number_process2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number2'] = message.text

        yes_no_kb = ReplyKeyboardMarkup(resize_keyboard=True)
        yes_no_kb.add(
            KeyboardButton("Да"),
            KeyboardButton("Нет")
        )

        await Form2.next()
        await message.reply(f'''Подтвердите ваши данные
Имя: {data['name2']}
Телефон: {data['phone_number2']}
        ''', reply_markup=yes_no_kb)



async def process_done(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        create_clients(data)

    await message.reply(
        "Спасибо. Мы с вами свяжемся.",
        reply_markup=ReplyKeyboardRemove()
    )