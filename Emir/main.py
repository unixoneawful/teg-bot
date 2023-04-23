from aiogram import Bot, Dispatcher, executor, types
import random
import os
from dotenv import load_dotenv
from os import getenv

load_dotenv()
BOT_TOKEN = '5968855267:AAFbYzvSVktlsgIl1VhOSwnekQ02BMMz6Ww'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text=f'Здравствуйте {message.from_user.first_name}, вас приветсвует NASA')
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=f'/start - начать\n'
                              f'/help - список всех команд\n'
                              f'/myinfo - получить информацию о себе\n'
                              f'/picture - показать случайную картинку')
    await message.delete()


@dp.message_handler(commands=['myinfo'])
async def myinfo_command(message: types.Message):
    await message.answer(text=f'Ваш id: {message.from_user.id}\n'
                              f'Ваше имя: {message.from_user.first_name}\n'
                              f'Ваш nickname: {message.from_user.username}\n')
    await message.delete()


@dp.message_handler(commands=['picture'])
async def nasa_picture(message: types.Message):
    with open('images/nasa.jpg', 'rb') as photo:
        await message.reply_photo(photo)


@dp.message_handler()
async def echo(message: types.Message):
    letters = message.text.split(' ')
    if len(letters) >= 3:
        await message.reply(message.text.upper())
    else:
        await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp)