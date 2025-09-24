"""
Tests for monsterrr-project-20250924-0413
"""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_create_and_get_item():
    # Create an item
    item_data = {"id": 1, "name": "Test Item", "description": "A test item"}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    assert response.json()["id"] == 1
    
    # Get the item
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"

def test_update_item():
    # Update the item
    updated_data = {"id": 1, "name": "Updated Item", "description": "An updated item"}
    response = client.put("/items/1", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Item"

def test_delete_item():
    # Delete the item
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert "message" in response.json()
    
    # Try to get the deleted item
    response = client.get("/items/1")
    assert response.status_code == 404
