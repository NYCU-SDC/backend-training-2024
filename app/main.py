from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel


app = FastAPI()

#Fast api 可以讓本機與網頁有互動，比如有人下了一個產品的訂單， 會傳進本機並從 database 取出id 對應的商品。
# http://localhost:8080/
@app.get("/")               
async def root():
    return {"message": "Hello World"}

# #定義一個網頁回傳鏈
# #http://localhost:8080/items/{item_id}?q={q}
# @app.get("/items/{item_id}") 
# async def read_item(item_id: int, q : str = None): # query 初始是 non 就不一定需要 在 網頁上有 q=
#     return {"item_id" : item_id , "q" : q}

#http://localhost:8080/users/{user_name}  #當他位於某一個 category 就放/items/{items}如果是 某個item 需要的參數比如 color就/items/{items}？colour=color 
# @app.get("/users/{user_name}")
# async def get_user(user_name : str):
#     return {"user_name":user_name}


# class UserId(int,Enum):
#     Alice = 1
#     Bob   = 3
#     Eve   = 5

# @app.get("/users/{user_id}")
# async def get_Users(user_id: UserId):
#     if user_id is UserId.Bob :
#         return {'user_id':user_id,'user_info':'someone who wants'}
    
#     if user_id.value == 3:
#         return { 'user_id':user_id,'user_info':'someone who wants'}
#     return {'user_id':user_id,'user_info':'someone who wants'}


# @app.get("/files/{file_path:path}") 
# async def read_file(file_path: str ):
#     return {"file_path" : file_path}


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