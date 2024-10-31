# .github/scripts/test_update_item.py
from fastapi.testclient import TestClient

try:
    from main import app  # Assuming the FastAPI application is in main.py
except ImportError:
    from app.main import app  # If unable to import from the main module, try importing from app.main


client = TestClient(app)

def test_update_item():
    item_id = 1
    data = {
        "name": "Test Item",
        "description": "A test description",
        "price": 10.5,
        "tax": 1.5
    }
    response = client.put(f"/items/{item_id}", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "item_id": item_id,
        "name": data["name"],
        "description": data["description"],
        "price": data["price"],
        "tax": data["tax"]
    }

def test_update_item_with_query():
    item_id = 1
    data = {
        "name": "Test Item",
        "description": "A test description",
        "price": 10.5,
        "tax": 1.5
    }
    query_param = "test_query"
    response = client.put(f"/items/{item_id}?q={query_param}", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "item_id": item_id,
        "name": data["name"],
        "description": data["description"],
        "price": data["price"],
        "tax": data["tax"],
        "q": query_param
    }
