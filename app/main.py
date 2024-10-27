from fastapi import FastAPI, Path, Query,HTTPException
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
'''
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

'''


@app.get("/items/{item_id}")
async def get_item(
    item_id: int,
    q: str = Query(None, max_length=50, min_length=3),  # 限制字串長度
    sort_order: str = "asc"
):
    # 檢查 item_id 是否在 1 到 1000 之間
    if not (1 <= item_id <= 1000):
        raise HTTPException(status_code=400, detail="item_id must be between 1 and 1000")
    
    # 如果提供了 q，則回傳包含 q 的描述
    if q is not None:
        return {
            "item_id": item_id,
            "description": f"This is a sample item that matches the query {q}.",
            "sort_order": sort_order
        }
    
    # 沒有提供 q 的情況
    return {
        "item_id": item_id,
        "description": "This is a sample item.",
        "sort_order": sort_order
    }


@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item,
    q: str = Query(None, max_length=50, min_length=3)
):
    # 檢查 item_id 是否在 1 到 1000 之間
    if not (1 <= item_id <= 1000):
        raise HTTPException(status_code=400, detail="item_id must be between 1 and 1000")
    
    # 檢查 q 是否提供並符合長度限制
    if q is not None:
        if len(q) < 3 or len(q) > 50:
            raise HTTPException(status_code=400, detail="Query 'q' must be between 3 and 50 characters.")
        # 返回帶有 q 的回應
        return {
            "item_id": item_id,
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "tax": item.tax,
            "q": q
        }
    
    # 如果 q 未提供，返回基本回應
    return {
        "item_id": item_id,
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "tax": item.tax
    }