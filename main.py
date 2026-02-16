from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import math
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Boss"}
@app.get("/ping")
def ping():
    return {"ping": "pong!"}

@app.get("/GET")
def get():
    return {"message": "Hello, nfactorial!"}

@app.get("/info", response_class=PlainTextResponse)
async def info(request: Request):
    return (
        f"{request.method}\n"
        f"{request.url}\n"
        f"HTTP/{request.scope.get('http_version')}"
    )
@app.post("/meaning-of-life",response_class=PlainTextResponse)
async def meaning_of_life():
    return {"meaning": "42"}

@app.get("/GET/{num}")
def get_num(num: int):
    num = math.factorial(num)
    return {"nfactorial": num}