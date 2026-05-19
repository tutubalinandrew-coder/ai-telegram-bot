import os
from fastapi import APIRouter, Depends
from schems import ChatRequest, ChatResponse, MessageResponse
from repository import count_user_messages, get_last_messages, get_or_create_user, delete_user_messages
from services import process_chat
from sqlalchemy.orm import Session
from dependencies import get_db, verify_api_key
from config import MEMORY_LIMIT





router = APIRouter(
    prefix="/api",
    tags=["chat"]
    )



@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
    ):
    answer = await process_chat(request, db)
    return {"answer": answer}




@router.get("/stats/{user_id}")
def get_stats (user_id: int, _: None =  Depends (verify_api_key)):
    count = count_user_messages(user_id)
    return{"user_id": user_id, "count_messages": count}

@router.get("/history/{user_id}")
def get_history(user_id: int, _: None =  Depends (verify_api_key)):
    history = get_last_messages(user_id, MEMORY_LIMIT)
    return {"user_id": user_id, "history": history}

@router.get("/users/{telegram_id}/messages", response_model=list[MessageResponse])
def get_messages(
    telegram_id: int,
    db: Session = Depends(get_db), 
    _: None =  Depends (verify_api_key)
    ):
    user = get_or_create_user(telegram_id, db)
    history = user.messages
    list_messages = []
    for msg in history:
        list_messages.append({
            "role": msg.role,
            "message": msg.message,
            "created_at": msg.created_at
        })

    return list_messages

@router.delete("/users/{telegram_id}/messages")
def delete_user(
    telegram_id: int, 
    db: Session = Depends(get_db),
    _: None =  Depends (verify_api_key)
    ):
    delete_user_messages(telegram_id, db)
    return {"status": "deleted"}
    