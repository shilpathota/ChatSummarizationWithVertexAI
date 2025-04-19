from fastapi import FastAPI, Request
from app.summarizer import summarize_chat


app = FastAPI()

@app.post("/summarize-chat")
async def summarize_chat_endpoint(request: Request):
    data = await request.json()
    return summarize_chat(data.get("chat_log", ""))