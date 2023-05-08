from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


async def sell_command(cb: types.CallbackQuery):
    '''
    Функция для того, чтобы пользователь продал авто
    '''
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text='Для продажи авто заполните форму /form'
    )


class Form(StatesGroup):
    name = State()
    phone_number = State()
    car_brand = State()
    car_price = State()
    address = State()


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply('Выход из формы')


async def form_start(message: types.Message):
    await Form.name.set()
    await message.reply('Введите ваше имя:')

async def name_process(message: types.Message, state: FSMContext):
    if not message.text.isalpha():
        await message.reply('Вводите только буквы!')
    else:
        async with state.proxy() as data:
            data = {}
            data['name'] = message.text

        await Form.next()
        await message.reply('Введите номер телефона:')


async def phone_number_process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data = {}
        data['phone_number'] = message.text

    await Form.next()
    await message.reply('Введите марку авто:')


async def car_brand_process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data = {}
        data['car_brand'] = message.text

    await Form.next()
    await message.reply('Введите цену вашего авто($):')


async def car_price_process(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.reply('Вводите только цифры!')
    else:
        async with state.proxy() as data:
            data = {}
            data['car_price'] = int(message.text)

        await Form.next()
        await message.reply('Введите ваш адрес:')


async def address_process(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data = {}
        data['address'] = message.text

    await Form.next()
    await message.reply('Форма заполнена')