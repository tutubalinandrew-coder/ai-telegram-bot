from fastapi import FastAPI
from schems import Message
from routes.chat import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
    return {"message": "API работает"}



    
@app.post("/echo")
def result(message: Message):
    return {"text": message.text}


