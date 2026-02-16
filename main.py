from fastapi import FastAPI, Request
app = FastAPI()
@app.get("/ping")
def ping():
    return {"ping": "pong!"}

@app.get("/info")
def info(request: Request):
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers)
    }