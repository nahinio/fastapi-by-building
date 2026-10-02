from pydantic import BaseModel

class armor(BaseModel):
    id: int
    name: str
    description: str
    category: str
    price: float
    available: bool

class items_response(BaseModel):
    status: str = "success"
    count: int
    items: list[armor]
