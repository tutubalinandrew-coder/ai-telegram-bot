from models import Message
from orm_database import SessionLocal

session = SessionLocal()
message = Message(
    user_id=1,
    role='user',
    message='hello'
)

session.add(message)
session.commit()

messages = session.query(Message).all()

for msg in messages:
    print(msg.id, msg.user_id, msg.role, msg.message)

session.close()
