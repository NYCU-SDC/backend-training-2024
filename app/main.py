from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
'''
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
'''
'''
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=10,min_length=3)] = 'Default'):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
'''
'''
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=10,min_length=3)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
'''
'''
@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query(max_length=10,min_length=3)] = ['12','23','12']):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
'''

'''
@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query(
            title="Query string!!!!",
            description="Query string for the items to search in the database that have a good match")] ):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

'''

'''
@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(alias="item_query")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

'''

# 定義請求體
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
@app.get("/")
async def read_main():
    return {"message": "Hello World"}

# 更新項目
@app.put("/items/{item_id}")
async def update_item(
    item_id: int = Path(..., description="The ID of the item to update"),
    item: Item = None,
    q: Optional[str] = Query(None)
):
    # 將 item_id 和更新的內容合併到返回結果中
    result = {"item_id": item_id, **item.dict()}
    
    # 如果 q 存在，將它加入到返回結果中
    if q:
        result["q"] = q
    
    return result
