from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


items = [
    {"id": 1, "name": "Notebook", "price": 4.99},
    {"id": 2, "name": "Pen", "price": 1.49},
]


@app.get("/")
def root():
    return {"message": "API is running"}


@app.get("/items")
def get_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items")
def create_item(item: Item):
    new_id = max([existing["id"] for existing in items], default=0) + 1
    new_item = {"id": new_id, "name": item.name, "price": item.price}
    items.append(new_item)
    return new_item
