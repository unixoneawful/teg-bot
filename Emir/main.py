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

import sqlite3
from pathlib import Path


# СУБД
# sqlite
# MySQL, Postgres, MariaDB

def init_db():
    """Для создания соединения с sqlite БД"""
    # DOCSTRING
    global db, cursor
    DB_NAME = 'db.sqlite'  # .sqlite, .db
    DB_PATH = Path(__file__).parent.parent
    db = sqlite3.connect(DB_PATH / DB_NAME)
    cursor = db.cursor()


def create_tables():
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS survey( 
        survey_id INTEGER PRIMARY KEY, 
        name TEXT, 
        age INTEGER, 
        gender TEXT, 
        user_id INTEGER 
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS products( 
        product_id INTEGER PRIMARY KEY, 
        name TEXT, 
        price INTEGER, 
        photo TEXT 
    )""")
    db.commit()


def delete_products():
    pass


def insert_products():
    """INSERT INTO products(name, price, photo)
        VALUES ('Самая лучшая книга', 200, 'images/cat.webp'),
        ('Самая интересная книга', 400, 'images/cat.webp'),
    """


def insert_survey(data, gender, user_id):
    # cursor.execute("""
    # INSERT INTO survey(name, age, gender, user_id)
    #     VALUES ("Daniel", 19, "male", 12312),
    #     ("Igor", 30, "male", 232323)
    # """)
    cursor.execute(""" 
    INSERT INTO survey(name, age, gender, user_id) 
        VALUES (:name, :age, :gender, :user_id), 

    """, {
        'name': data.get('name'),
        'age': data.get('age'),
        'gender': gender,
        'user_id': user_id
    })
    db.commit()