from pydantic import BaseModel
from datetime import datetime

class ChatRequest(BaseModel):
    user_id: int
    text: str

class ChatResponse(BaseModel):
    answer: str

class MessageResponse(BaseModel):
    role: str
    message: str
    created_at: datetime