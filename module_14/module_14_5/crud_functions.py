import sqlite3
import os
import random as rand

connection = sqlite3.connect('initiate_db.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER
    )
    ''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_title ON Products (title)')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL DEFAULT 1000
    )
    ''')


def initialize_db():
    products = os.listdir("./img")
    products = [os.path.splitext(product)[0] for product in products]
    for product in products:
        cursor.execute('INSERT INTO Products (title, description, price) VALUES(?,?,?)',
                       (f'{product}', f'{product}', rand.randint(900, 1000)))
    connection.commit()
    print("Database created successfully!")


def update_product(product_id: int, title: str, description: str, price: int):
    cursor.execute('UPDATE Products SET title=?, description=?, price=? WHERE id=?',
                   (title, description, price, product_id))
    connection.commit()


def delete_db():
    os.remove('initiate_db.db')


def add_product(title, description, price):
    check_title = cursor.execute('SELECT * FROM Products WHERE title=?', (title,))
    if check_title.fetchone() is None:
        cursor.execute('INSERT INTO Products (title, description, price) VALUES(?,?,?)',
                       (title, description, price))
    connection.commit()


def get_product_by_id(product_id: int):
    cursor.execute('SELECT * FROM Products WHERE id =?', (product_id,))
    return cursor.fetchone()[0]


def get_product_by_title(product_title: str):
    cursor.execute('SELECT * FROM Products WHERE title =?', (product_title,))
    return cursor.fetchone()[0]


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()


def add_user(username, email, age):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)',
                   (username, email, age))
    connection.commit()


def is_included(username):
    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    return cursor.fetchone() is not None


connection.commit()
