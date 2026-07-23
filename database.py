import sqlite3
from config import DATABASE_NAME

def connect_db():
    return sqlite3.connect(DATABASE_NAME)

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        full_name TEXT,
        username TEXT,
        lesson INTEGER DEFAULT 1,
        quiz_score INTEGER DEFAULT 0,
        completed INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()

def add_user(user_id, full_name, username):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO users
    (user_id, full_name, username)
    VALUES (?, ?, ?)
    """, (user_id, full_name, username))

    conn.commit()
    conn.close()

def get_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM users
    WHERE user_id = ?
    """, (user_id,))

    user = cursor.fetchone()

    conn.close()

    return user

def update_lesson(user_id, lesson):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE users
    SET lesson = ?
    WHERE user_id = ?
    """, (lesson, user_id))

    conn.commit()
    conn.close()

def complete_course(user_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE users
    SET completed = 1
    WHERE user_id = ?
    """, (user_id,))

    conn.commit()
    conn.close()
