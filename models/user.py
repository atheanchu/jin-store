from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import List, Optional


class User(SQLModel, table=True):
    username: str = Field(primary_key=True, index=True)
    password: str
    first_name: str
    last_name: str
    create_date: datetime
    address: Optional[str] = None
    phone_number: Optional[str] = None

    orders: List["Order"] = Relationship(back_populates="users")

    class Settings:
        name = "user"

    model_config = {
        "json_schema_extra": {
            "example": [
                {
                    "username": "ironman",
                    "password": "strong!!!",
                    "first_name": "Tony",
                    "last_name": "Stark",
                }
            ]
        }
    }
