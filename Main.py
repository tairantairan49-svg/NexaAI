from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "NexaAI Backend Chal Gaya 🔥"}

@app.get("/hello")
def hello():
    return {"message": "Hello from NexaAI"}
