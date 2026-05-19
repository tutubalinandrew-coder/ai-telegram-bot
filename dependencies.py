from config import SECRET_KEY
from orm_database import SessionLocal
from fastapi import HTTPException, Header

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_api_key(api_key: str = Header()):
    if api_key != SECRET_KEY:
        raise HTTPException(status_code=403)