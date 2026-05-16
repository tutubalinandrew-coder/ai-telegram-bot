from pydantic import BaseModel


class Message(BaseModel):
    user_id: int
    text: str

class ChatResponse(BaseModel):
    answer: str

