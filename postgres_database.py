import psycopg
from config import (POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT)

def connect_postgres():
    connection = psycopg.connect(
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT
    )
    return connection


def create_messages_table():
    connection = connect_postgres()
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY,
    user_id BIGINT,
    role TEXT,
    message TEXT)''')
    connection.commit()
    connection.close()

def save_message(user_id, role, message):
    connection = connect_postgres()
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO messages (user_id, role, message)
    VALUES (%s, %s, %s)''',
    (user_id, role, message)
    )
    connection.commit()
    connection.close()

def get_last_messages(user_id, limit):
    connection = connect_postgres()
    cursor = connection.cursor()
    cursor.execute('''
    SELECT role, message
    FROM messages
    WHERE user_id = %s
    ORDER BY id DESC
    LIMIT %s''',
    (user_id, limit))
    messages = cursor.fetchall()
    connection.close()
    return messages

def delete_user_messages(user_id):
    connection = connect_postgres()
    cursor = connection.cursor()
    cursor.execute('''
    DELETE FROM messages
    WHERE user_id = %s''',
    (user_id,))
    connection.commit()
    connection.close()


def count_user_messages(user_id):
    connection = connect_postgres()
    cursor = connection.cursor()
    cursor.execute('''
    SELECT COUNT(*) FROM messages
    WHERE user_id = %s''',
    (user_id,))
    result = cursor.fetchone()
    connection.close()
    return result[0]
