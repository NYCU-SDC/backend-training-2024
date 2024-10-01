

from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel


app = FastAPI()

#Fast api 可以讓本機與網頁有互動，比如有人下了一個產品的訂單， 會傳進本機並從 database 取出id 對應的商品。
# http://localhost:8080/
@app.get("/")               
async def root():
    return {"message": "Hello World"}

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result