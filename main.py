from fastapi import FastAPI
import time
import asyncio


app=FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(3)
    return {
        "message":"Async Api"
    }
