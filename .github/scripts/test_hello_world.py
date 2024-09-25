# .github/scripts/test_hello_world.py
import pytest
from fastapi.testclient import TestClient

try:
    from main import app  # Assuming the FastAPI application is in main.py
except ImportError:
    from app.main import app  # If unable to import from the main module, try importing from app.main


client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}  # Adjust based on your FastAPI response
    
