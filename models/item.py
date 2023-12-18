from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime


class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: int
    description: str = None
    create_date: datetime
    image: str = None

    class Settings:
        name = "item"

    model_config = {"json_schema_extra": {"example": [{"name": "ipad", "price": 1500000}]}}

    orders: List["Order"] = Relationship(back_populates="items")
