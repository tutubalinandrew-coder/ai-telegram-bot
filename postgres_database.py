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


