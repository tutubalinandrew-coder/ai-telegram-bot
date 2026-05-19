from models import Message, User
from orm_database import SessionLocal



def get_session(db):
    if db is not None:
        return db, False

    return SessionLocal(), True


def save_message(user_id, role, message, db=None, user_id_db=None):
    db, should_close =  get_session(db)
    if user_id_db is None:
        user = get_or_create_user(user_id, db)
        print(user.messages)
        user_id_db = user.id
    new_message = Message(
        user_id=user_id,
        role=role,
        message=message,
        user_id_db=user_id_db
        )
    db.add(new_message)
    db.commit()
    if should_close:
        db.close()



def get_last_messages(user_id, limit, db=None):
    db, should_close =  get_session(db)
    message = db.query(Message)
    message = message.filter(Message.user_id == user_id)
    message = message.order_by(Message.id.desc())
    message = message.limit(limit)
    messages = message.all()
    result = []
    for msg in messages:
        result.append((msg.role, msg.message))
    if should_close:
        db.close()    
    return result
         

def delete_user_messages(user_id, db=None):
    db, should_close =  get_session(db)
    message = db.query(Message)
    message = message.filter(Message.user_id == user_id)
    message.delete()
    db.commit()
    if should_close:
        db.close()  




def count_user_messages(user_id, db=None):
    db, should_close =  get_session(db)
    message = db.query(Message)
    message = message.filter(Message.user_id == user_id)
    message = message.count()
    if should_close:
        db.close()  
    return message

def get_or_create_user(telegram_id, db=None):
    db, should_close =  get_session(db)
    tg_id = db.query(User)
    tg_id = tg_id.filter(User.telegram_id == telegram_id)
    tg_id = tg_id.first()
    if tg_id is None:
        new_user = User(telegram_id=telegram_id)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        if should_close:
            db.close()
        return new_user
    if should_close:
        db.close()
    return tg_id


        