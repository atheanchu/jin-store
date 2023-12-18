from models import User, Item
from datetime import datetime
from .database import get_session
from sqlmodel import select
import json


# Initialize Users table with three users
async def initialize_users():
    db = next(get_session())
    statement = select(User)
    # We don't need to initialize if there's data in the table
    # if db.get(User, 1):
    if db.exec(statement).first():
        return

    ironman = User(
        username="ironman",
        password="passw0rd",
        first_name="Tony",
        last_name="Stark",
        create_date=datetime.now(),
    )

    captain_america = User(
        username="captainamerica",
        password="passw0rd",
        first_name="Steve",
        last_name="Rogers",
        create_date=datetime.now(),
    )

    thor = User(
        username="thor",
        password="passw0rd",
        first_name="Thor",
        last_name="Odinson",
        create_date=datetime.now(),
    )

    db.add(ironman)
    db.add(captain_america)
    db.add(thor)

    db.commit()
    db.close()


async def initialize_items():
    db = next(get_session())
    statement = select(Item)

    # We don't need to initialize if there's data in the table
    if db.exec(statement).first():
        return

    # Load Json file ./data/items.json and save it to items
    with open("./utils/data/items.json", "r") as f:
        items = json.load(f)

        for item in items:
            new_item = Item(
                name=item["name"],
                price=item["price"],
                description=item["description"],
                image=item["image"],
                create_date=datetime.now(),
            )
            db.add(new_item)

    db.commit()
    db.close()
