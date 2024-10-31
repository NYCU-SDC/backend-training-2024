# .github/scripts/test_homework3.py
from fastapi.testclient import TestClient

try:
    from main import app  # Assuming the FastAPI application is in main.py
except ImportError:
    from app.main import app  # If unable to import from the main module, try importing from app.main

client = TestClient(app)

# Test the correctness of GET /items/{item_id}
def test_get_item_valid():
    response = client.get("/items/123?q=test_query&sort_order=asc")
    assert response.status_code == 200
    assert response.json() == {
        "item_id": 123,
        "description": "This is a sample item that matches the query test_query",
        "sort_order": "asc"
    }

# Test GET /items/{item_id} with invalid path parameter
def test_get_item_invalid_id():
    response = client.get("/items/1001")
    assert response.status_code == 422  # Should return 422 Unprocessable Entity
    assert "detail" in response.json()

# Test GET /items/{item_id} with invalid query parameter q
def test_get_item_invalid_query():
    response = client.get("/items/123?q=ab&sort_order=asc")
    assert response.status_code == 422  # Should return 422 Unprocessable Entity
    assert "detail" in response.json()

# Test GET /items/{item_id} without query parameters
def test_get_item_no_query():
    response = client.get("/items/123")
    assert response.status_code == 200
    assert response.json() == {
        "item_id": 123,
        "description": "This is a sample item.",
        "sort_order": "asc"
    }

# Test PUT /items/{item_id} to update item data
def test_put_item_valid():
    data = {
        "name": "Updated Item",
        "description": "Updated item description",
        "price": 20.0,
        "tax": 2.5
    }
    response = client.put("/items/123", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "item_id": 123,
        "name": "Updated Item",
        "description": "Updated item description",
        "price": 20.0,
        "tax": 2.5
    }

# Test PUT /items/{item_id} with valid query parameter q
def test_put_item_with_query():
    data = {
        "name": "Updated Item",
        "description": "Updated item description",
        "price": 20.0,
        "tax": 2.5
    }
    response = client.put("/items/123?q=test_query", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "item_id": 123,
        "name": "Updated Item",
        "description": "Updated item description",
        "price": 20.0,
        "tax": 2.5,
        "q": "test_query"
    }

# Test PUT /items/{item_id} with invalid path parameter
def test_put_item_invalid_id():
    data = {
        "name": "Updated Item",
        "description": "Updated item description",
        "price": 20.0,
        "tax": 2.5
    }
    response = client.put("/items/1001", json=data)
    assert response.status_code == 422
    assert "detail" in response.json()

# Test PUT /items/{item_id} with invalid query parameter q
def test_put_item_invalid_query():
    data = {
        "name": "Updated Item",
        "description": "Updated item description",
        "price": 20.0,
        "tax": 2.5
    }
    response = client.put("/items/123?q=ab", json=data)
    assert response.status_code == 422
    assert "detail" in response.json()
