from aiogram import types
from handlers import constans


async def qwerty(message: types.Message):
    '''
    Функция ответа пользователю
    '''
    await message.answer(text=constans.ANSWER_BOT)