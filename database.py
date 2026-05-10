
import sqlite3



def connect_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    return connection, cursor

def create_messages_table():
    connection, cursor = connect_db()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    role TEXT,
    message TEXT)
    ''')
    connection.commit()
    connection.close()

def save_message(user_id, role, message):
    connection, cursor = connect_db()
    cursor.execute('''
    INSERT INTO messages (
    user_id, role, message)
    VALUES (?, ?, ?)
    ''',
    (user_id, role, message)
    )
    connection.commit()
    connection.close()

def get_all_messages():
    connection, cursor = connect_db()
    cursor.execute('''
    SELECT * FROM messages''')
    messages = cursor.fetchall()
    connection.close()
    return messages

def get_last_messages(user_id, limit):
    connection, cursor = connect_db()
    cursor.execute('''
    SELECT role, message
    FROM messages    
    WHERE user_id = ?
    ORDER BY id DESC
    LIMIT ?
    ''',
    (user_id, limit))
    messages = cursor.fetchall()
    connection.close()
    return messages

def delete_user_messages(user_id):
    connection, cursor = connect_db()
    cursor.execute('''
    DELETE FROM messages
    WHERE user_id = ?''',
    (user_id,))
    connection.commit()
    connection.close()

def count_user_messages(user_id):
    connection, cursor = connect_db()
    cursor.execute('''
    SELECT COUNT(*) FROM messages
    WHERE user_id = ?''',
    (user_id,))
    result = cursor.fetchone()
    connection.close()
    return result[0]