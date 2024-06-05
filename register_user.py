import sqlite3
from werkzeug.security import generate_password_hash
import argparse

DATABASE = 'database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def register_user(username, email, password, is_admin):
    hashed_password = generate_password_hash(password)
    db = get_db()
    try:
        db.execute('INSERT INTO users (username, email, password, is_admin) VALUES (?, ?, ?, ?)', (username, email, hashed_password, is_admin))
        db.commit()
        print("User registered successfully")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Register a new user')
    parser.add_argument('username', type=str, help='Username of the new user')
    parser.add_argument('email', type=str, help='Email of the new user')
    parser.add_argument('password', type=str, help='Password of the new user')
    parser.add_argument('--admin', action='store_true', help='Set the user as admin')

    args = parser.parse_args()
    register_user(args.username, args.email, args.password, args.admin)
