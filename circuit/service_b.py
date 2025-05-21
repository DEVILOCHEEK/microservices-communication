from fastapi import FastAPI
import random
import time

app = FastAPI()

@app.get("/unstable")
async def unstable():
    if random.random() < 0.5:
        time.sleep(3)
        return "Delayed response"
    return "Quick response"
