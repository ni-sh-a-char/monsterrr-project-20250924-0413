"""
monsterrr-project-20250924-0413 - Auto-generated project by Monsterrr
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI(title="monsterrr-project-20250924-0413", description="Auto-generated project by Monsterrr")

class Item(BaseModel):
    id: int
    name: str
    description: str = None

# In-memory storage
items: List[Item] = []

@app.get("/")
async def root():
    return {"message": "Welcome to monsterrr-project-20250924-0413 API"}

@app.get("/items/", response_model=List[Item])
async def get_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    for i, item in enumerate(items):
        if item.id == item_id:
            items[i] = updated_item
            return updated_item
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for i, item in enumerate(items):
        if item.id == item_id:
            items.pop(i)
            return {"message": "Item deleted"}
    return {"error": "Item not found"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
