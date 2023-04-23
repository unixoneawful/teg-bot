from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

buy_kb = ReplyKeyboardMarkup(resize_keyboard=True)
buy_kb.add(
    KeyboardButton('C class'),
    KeyboardButton('E class'),
    KeyboardButton('S class')
)

async def buy_command(cb: types.CallbackQuery):
    '''
    Функция для того, чтобы пользователь купил авто
    '''
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text='Выберите категорию авто',
        reply_markup=buy_kb
    )