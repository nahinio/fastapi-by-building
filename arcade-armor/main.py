from fastapi import FastAPI, Query, HTTPException
from models import armor, items_response
from data import armor_items


app = FastAPI(
    title="Arcade Armor - Retro Arcade Game Item Shop",
    description="Read only Rest API for the Arcade Armor retro arcade game item shop. This API allows you to retrieve information about available items and other relevant details."
)


@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Arcade Armor API! Use the endpoints to explore available items and their details."
    }


# /items -> path operation to retrieve all items
# /items?category=armor&available=true -> path operation to retrieve items filtered by category and availability


@app.get("/armor-items", response_model=items_response)    # response_model=items_response is basically dependency injection, it will automatically convert the response to the specified model
def read_items(category: str | None = Query(default=None, description="Filter items by category (e.g., armor, weapon, accessory)")):
    if category:
        filtered_items = [item for item in armor_items if item["category"] == category.lower()]
        if not filtered_items:
            raise HTTPException(status_code=404, detail=f"No items found in category '{category}'")

        return items_response(
            count=len(filtered_items), 
            items=filtered_items    # type: ignore
        )    
    return items_response(
        count=len(armor_items),
        items=armor_items    # type: ignore
    )    


@app.get("/armor-items/{item_id}", response_model=armor)
def read_item(item_id: int):
    for item in armor_items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")