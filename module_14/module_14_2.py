import sqlite3
import random as rand

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
    ''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)',
                   (f'User_{i}', f'example{i}@gmail.com', i * 10, 1000))
for i in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE username = ?',
                   (500, f'User_{i}'))
#
for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE username = ?', (f'User_{i}',))

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

cursor.execute('SELECT COUNT(*) FROM Users')
count_users = cursor.fetchone()[0]
print(f'Count users  = {count_users}')

cursor.execute('SELECT SUM(balance) FROM Users')
balance_sum = cursor.fetchone()[0]
print(f'Total balance = {balance_sum}')

print(f'Average age = {balance_sum/count_users:.2f}')

connection.commit()
connection.close()
