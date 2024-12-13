import sqlite3
import random as rand

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL
    )
    ''')

# cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
# for i in range(1, 31):
#     cursor.execute('INSERT INTO Users (username, email, age) VALUES(?, ?, ?)',
#                    (f'new_user{i}', f'{i}test@urban.test', rand.randint(20, 60)))
for _ in range(20):
    cursor.execute('UPDATE users SET age = ? WHERE username = ?',
                   (rand.randint(20, 60), f'new_user{rand.randint(1, 30)}'))

# cursor.execute('DELETE FROM Users WHERE username = ?', ('new_user1',))

# cursor.execute('SELECT * FROM Users')
# users = cursor.fetchall()
#
# for user in users:
#     print(user)

# cursor.execute('SELECT username, age FROM Users WHERE age > ?', (45,))
# above_45 = cursor.fetchall()
#
# for user in above_45:
#     print(user)

cursor.execute(" SELECT username, age FROM Users GROUP BY AGE")
average_age = cursor.fetchall()
for user in average_age:
    print(user)
cursor.execute("SELECT max(age) FROM Users")
total1 = cursor.fetchone()[0]
total2 = cursor.fetchall()
print(total1)
print(total2)


connection.commit()
connection.close()
