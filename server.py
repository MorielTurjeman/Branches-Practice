
from fastapi import FastAPI
import uvicorn
from fastapi import Request

app = FastAPI()

@app.get('/sanity')
async def get_sanity():
    return "Server is up and running smoothly"