import sqlite3
from pathlib import Path

def init():
    global db, cur
    # global cur
    DB_NAME = 'db.sqlite3'
    MAIN_PATH = Path(__file__).parent.parent
    db = sqlite3.connect(MAIN_PATH / DB_NAME)
    cur = db.cursor()

def create_table():
    '''
    для создания таблицы с автомобилямив БД
    '''
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS products(
        product_id INTEGER PRIMARY KEY,
        name TEXT,
        descr TEXT,
        price TEXT,
        photo TEXT
        )
        '''
    )
    db.commit()

def create_table2():
    '''
    создание таблицы покупателей
    '''
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS clients(
        client_id INTEGER PRIMARY KEY,
        name TEXT,
        phone_number TEXT,
        product_id INTEGER, 
        FOREIGN KEY (product_id)
            REFERENCES products (product_id)
                ON DELETE CASCADE)
        '''
    )
    db.commit()

def populate_products():
    '''
    заполняем таблицу с автомобилями
    '''
    cur.execute(
        '''
        INSERT INTO products(
        name,
        descr,
        price,
        photo)
        VALUES
        ('Mercedes-Benz', 'class - C', '8000$', './images/6ff264as-960.jpg'),
        ('Mercedes-Benz', 'class - C', '9200$', './images/hqdefault.jpg'), 
        ('Mercedes-Benz', 'class - E', '12000$', './images/e124.jpg'),
        ('Mercedes-Benz', 'class - E', '10100$', './images/e140.jpg'),
        ('Mazda Primacy', 'class - S', '20000$', './images/mazda.jpeg'),
        ('Subaru Legacy', 'class - S', '45000$', './images/sub.jpg') 
        '''
    )
    db.commit()



def get_products():
    cur.execute(
        '''
        SELECT * FROM products
        '''
    )
    return cur.fetchall()

def create_clients(data):
    """
        Заполняем таблицу clients
    """
    data = data.as_dict()
    cur.execute(
        '''
        INSERT INTO clients(
        name,
        phone_number,
        product_id
        ) VALUES (:name,:phone_number,:product_id)''',
                {'name': data['name2'],
                'phone_number': data['phone_number2'],
                'product_id': data['product_id']})
    db.commit()


init()
create_table2()
create_table()
# populate_products()
get_products()


