from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime


class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    order_date: datetime
    username: str = Field(foreign_key="user.username")
    item_id: int = Field(foreign_key="item.id")

    users: List["User"] = Relationship(back_populates="orders")
    items: List["Item"] = Relationship(back_populates="orders")

    class Settings:
        name = "order"

    model_config = {"json_schema_extra": {"example": [{"username": "ironman", "item_id": 1}]}}


class OrderCreate(SQLModel):
    username: str
    item_id: int


class OrderRead(SQLModel):
    id: int
    username: str
    item_name: str
    order_date: datetime
