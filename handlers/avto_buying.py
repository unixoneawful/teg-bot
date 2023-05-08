from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from db.database import get_products

def buy_kb(product_id):
    car_kb = InlineKeyboardMarkup()
    car_kb.add(InlineKeyboardButton('Купить', callback_data=f'form_start2 {product_id}'))

    return car_kb


async def car_c(message: types.Message):
    '''
    СПИСОК АBTО
    '''
    c_class1 = get_products()[0]
    c_class2 = get_products()[1]
    await message.answer(text='Все автомобили класса -С-')
    await message.answer_photo(open(f'{c_class1[4]}', 'rb'),
                               caption=f'Марка: {c_class1[1]}\n'
                                       f'Класс: {c_class1[2]}\n'
                                       f'Цена: {c_class1[3]}',
                               reply_markup=buy_kb(c_class1[0]))
    await message.answer_photo(open(f'{c_class2[4]}', 'rb'),
                               caption=f'Марка: {c_class2[1]}\n'
                                       f'Класс: {c_class2[2]}\n'
                                       f'Цена: {c_class2[3]}',
                               reply_markup=buy_kb(c_class2[0]))


async def car_e(message: types.Message):
    '''
    СПИСОК АBTО
    '''
    e_class1 = get_products()[2]
    e_class2 = get_products()[3]
    await message.answer(text='Все автомобили класса -E-')
    await message.answer_photo(open(f'{e_class1[4]}', 'rb'),
                               caption=f'Марка: {e_class1[1]}\n'
                                       f'Класс: {e_class1[2]}\n'
                                       f'Цена: {e_class1[3]}',
                               reply_markup=buy_kb(e_class1[0]))
    await message.answer_photo(open(f'{e_class2[4]}', 'rb'),
                               caption=f'Марка: {e_class2[1]}\n'
                                       f'Класс: {e_class2[2]}\n'
                                       f'Цена: {e_class2[3]}',
                               reply_markup=buy_kb(e_class2[0]))


async def car_s(message: types.Message):
    '''
    СПИСОК АBTО
    '''
    s_class1 = get_products()[4]
    s_class2 = get_products()[5]
    await message.answer(text='Все автомобили класса -S-')
    await message.answer_photo(open(f'{s_class1[4]}', 'rb'),
                               caption=f'Марка: {s_class1[1]}\n'
                                       f'Класс: {s_class1[2]}\n'
                                       f'Цена: {s_class1[3]}',
                               reply_markup=buy_kb(s_class1[0]))
    await message.answer_photo(open(f'{s_class2[4]}', 'rb'),
                               caption=f'Марка: {s_class2[1]}\n'
                                       f'Класс: {s_class2[2]}\n'
                                       f'Цена: {s_class2[3]}',
                               reply_markup=buy_kb(s_class2[0]))