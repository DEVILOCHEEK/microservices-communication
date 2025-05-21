rom fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/gateway/service-a")
async def service_a():
    async with httpx.AsyncClient() as client:
        res = await client.get("http://localhost:5000/data")
        return res.json()

@app.get("/gateway/service-b")
async def service_b():
    async with httpx.AsyncClient() as client:
        res = await client.get("http://localhost:5001/data")
        return res.json()
