import sqlite3

connection = sqlite3.connect('products.db')
cursor = connection.cursor()

def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('''
           CREATE TABLE IF NOT EXISTS Users(
           id INTEGER PRIMARY KEY,
           username TEXT NOT NULL,
           email TEXT NOT NULL,
           age INTEGER NOT NULL,
           balance INTEGER NOT NULL)''')
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")

    #connection = sqlite3.connect('products.db')
    #cursor = connection.cursor()
    cursor.execute('DELETE FROM Products')
    cursor.execute('''  
    CREATE TABLE IF NOT EXISTS Products(     
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL)''')
    for i in range(1, 5):
        cursor.execute(
                'INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
            (f'Продукт {i}', f'Описание {i}', i * 100)
                      )
        initiate_db()

def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id, title, description, price FROM Products')
    db = cursor.fetchall()

    connection.commit()
    connection.close()
    return list(db)

def add_user(username, email, age):
    cursor.execute(f"INSERT INTO Users (username, email, age, balance ) VALUES(?, ?, ?, ?)",
                   (f'{username}', f'{email}', age, 1000))

def is_included(username):
    check_user = cursor.execute('SELECT * FROM Users WHERE username=?', (username,))
    if check_user.fetchone():
        return True
    else:
        return False

connection.commit()