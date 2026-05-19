from fastapi import FastAPI
import time
from schems import ChatRequest
from routes.chat import router
from logger import logger
from fastapi import Request
from fastapi.responses import JSONResponse




app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
    return {"message": "API работает"}



    
@app.post("/echo")
def result(request: ChatRequest):
    return {"text": request.text}

@app.middleware("http")
async def log_requests(request: Request, call_next):
    time_before = time.time()
    response = await call_next(request)
    
    time_after = time.time()
    result_time = time_after - time_before
    logger.info(
    f"{request.method} "
    f"{request.url.path} "
    f"{response.status_code} "
    f"{result_time:.4f}s"
    )
    return response


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Ошибка на {request.method} {request.url.path}: {exc}")

    return JSONResponse(
        status_code=500,
        content={"detail": "Внутренняя ошибка сервера"}
    )
