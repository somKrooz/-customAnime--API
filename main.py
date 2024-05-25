from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from data import getData , getAll , getBranched

app = FastAPI()

class Post(BaseModel):
    title: str
    isCool: Optional[bool] = True

#Give me my money
@app.get('/')
async def root():
    return {"Hello": "World"}

@app.get('/krooz')
async def krooz():
   json = getAll()
   return json


@app.get('/post')
async def post(title):
    json = getData(title)
    return json

@app.get("/anime")
async def anime():
    json = getBranched()
    return json


