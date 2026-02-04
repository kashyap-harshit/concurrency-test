from fastapi import FastAPI
import asyncio
app = FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(5)
    return "ASGI response after 5 seconds"