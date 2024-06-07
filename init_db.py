import sqlite3
from werkzeug.security import generate_password_hash

def init_db():
    with open('schema.sql') as f:
        schema = f.read()
    
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.executescript(schema)

    # Admin user creation
    hashed_password = generate_password_hash('123456', method='pbkdf2:sha256')
    cursor.execute("INSERT INTO users (username, email, password, is_admin) VALUES (?, ?, ?, ?)",
                ('admin', 'admin@blog.com', hashed_password, 1))

    cursor.execute("INSERT INTO users (username, email, password, is_admin) VALUES (?, ?, ?, ?)",
                ('kagan', 'kagan@blog.com', hashed_password, 0))

    cursor.execute("INSERT INTO users (username, email, password, is_admin) VALUES (?, ?, ?, ?)",
                ('ali', 'ali@blog.com', hashed_password, 0))

    connection.commit()
    connection.close()


if __name__ == '__main__':
    init_db()
