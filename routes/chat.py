from fastapi import APIRouter, Depends
from schems import Message, ChatResponse
from repository import count_user_messages, get_last_messages
from services import process_chat
from sqlalchemy.orm import Session
from dependencies import get_db



router = APIRouter(
    prefix="/api",
    tags=["chat"]
    )



@router.post("/chat", response_model=ChatResponse)
async def chat(
    message: Message,
    db: Session = Depends(get_db)
    ):
    answer = await process_chat(message, db)
    return {"answer": answer}




@router.get("/stats/{user_id}")
def get_stats (user_id: int):
    count = count_user_messages(user_id)
    return{"user_id": user_id, "count_messages": count}

@router.get("/history/{user_id}")
def get_history(user_id: int):
    history = get_last_messages(user_id, 20)
    return {"user_id": user_id, "history": history}