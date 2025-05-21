from fastapi import FastAPI
import httpx
from tenacity import retry, stop_after_attempt, wait_fixed

app = FastAPI()

@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
async def call_service_b():
    async with httpx.AsyncClient() as client:
        res = await client.get("http://localhost:8001/unstable")
        return res.text

@app.get("/call")
async def call():
    try:
        result = await call_service_b()
        return {"result": result}
    except:
        return {"error": "Service B is down"}
