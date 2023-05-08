

from aiogram import executor
from aiogram.dispatcher.filters import Text
from config import dp


'''импорт функций'''
from handlers.answer import qwerty
from handlers.reminder import schedule_command
from handlers.reminder import remind_command
from handlers.reminder import schedule
from handlers.start import start_command
from handlers.buy import buy_command
from handlers.sell import sell_command
from handlers.avto_buying import car_c, car_e, car_s
from webparsing.answer_cars import show_cars


'''импорт функций формы продать'''
from handlers.sell import Form
from handlers.sell import cancel_handler
from handlers.sell import (
    form_start,
    name_process,
    phone_number_process,
    car_brand_process,
    car_price_process,
    address_process
)


'''импорт функций формы купить'''
from handlers.cupit_form import kupit_command
from handlers.cupit_form import Form2
from handlers.cupit_form import cancel_handler2
from handlers.cupit_form import process_done
from handlers.cupit_form import (
    form_start2,
    name_process2,
    phone_number_process2,

)


'''импорт базы данных'''
from db.database import (
init,
create_table,
create_table2
)

from webparsing.data_cars_parsing import (
init1,
create_table_cars
)

from webparsing.parsing import get_cars

import asyncio
async def startup(_):
    """
        запускаем дополнительные сторонние сервисы
    """
    init()
    create_table()
    create_table2()
    asyncio.create_task(schedule())
    init1()
    create_table_cars()
    get_cars()


if __name__ == '__main__':

    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(show_cars, commands=['cars'])
    dp.register_callback_query_handler(buy_command, text='buy_command')
    dp.register_message_handler(car_c, Text(equals='C class'))
    dp.register_message_handler(car_e, Text(equals='E class'))
    dp.register_message_handler(car_s, Text(equals='S class'))
    '''форма продать'''
    dp.register_callback_query_handler(sell_command, text='sell_command')
    dp.register_message_handler(form_start, commands=['form'])
    dp.register_message_handler(cancel_handler, state='*', commands='cancel')
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(name_process, state=Form.name)
    dp.register_message_handler(phone_number_process, state=Form.phone_number)
    dp.register_message_handler(car_brand_process, state=Form.car_brand)
    dp.register_message_handler(car_price_process, state=Form.car_price)
    dp.register_message_handler(address_process, state=Form.address)
    '''форма купить'''
    dp.register_callback_query_handler(kupit_command, text='kupit_command')
    dp.register_message_handler(cancel_handler2, state='*', commands='cancel')
    dp.register_message_handler(cancel_handler2, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(name_process2, Text(equals='Нет'), state=Form2.done)
    dp.register_callback_query_handler(form_start2, Text(startswith=['form_start2']))
    dp.register_message_handler(name_process2, state=Form2.name2)
    dp.register_message_handler(phone_number_process2, state=Form2.phone_number2)
    dp.register_message_handler(process_done, Text(equals='Да'), state=Form2.done)
    '''напоминалка'''
    dp.register_message_handler(remind_command, commands=['remind'])
    dp.register_message_handler(schedule_command, Text(startswith='напомни'))
    dp.register_message_handler(qwerty)

    executor.start_polling(dp, skip_updates=True, on_startup=startup)