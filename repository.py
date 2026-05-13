from unittest import result
from sqlalchemy.orm import query
from models import Message
from orm_database import SessionLocal
from postgres_database import connect_postgres




def save_message(user_id, role, message):
    with SessionLocal() as session:
        message = Message(
            user_id=user_id,
            role=role,
            message=message
            )
        session.add(message)
        session.commit()



def get_last_messages(user_id, limit):
    with SessionLocal() as session:
        message = session.query(Message)
        message = message.filter(Message.user_id == user_id)
        message = message.order_by(Message.id.desc())
        message = message.limit(limit)
        messages = message.all()
        result = []
        for msg in messages:
            result.append((msg.role, msg.message))
            
        return result
         

def delete_user_messages(user_id):
    with SessionLocal() as session:
        message = session.query(Message)
        message = message.filter(Message.user_id == user_id)
        message.delete()
        session.commit()




def count_user_messages(user_id):
    with SessionLocal() as session:
        message = session.query(Message)
        message = message.filter(Message.user_id == user_id)
        message = message.count()
        return message