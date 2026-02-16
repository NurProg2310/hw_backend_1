from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Boss"}
@app.get("/ping")
def ping():
    return {"ping": "pong!"}

@app.get("/info", response_class=PlainTextResponse)
async def info(request: Request):
    return (
        f"{request.method}\n"
        f"{request.url}\n"
        f"HTTP/{request.scope.get('http_version')}"
    )
@app.post("/meaning-of-life")
def meaning_of_life():
    return {"meaning": "42"}