from sqlmodel import SQLModel, Session, create_engine, Field
from dotenv import load_dotenv
from models import User, Item, Order
import os
from typing import Optional

load_dotenv()

db_url = os.getenv("DATABASE_URL")
db_user = os.getenv("DATABASE_USER")
db_password = os.getenv("DATABASE_PASSWORD")
# DATABASE_URL = f"postgresql://{db_user}:{db_password}@127.0.0.1/moomarket"
DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_url}/moomarket"


engine_url = create_engine(DATABASE_URL, echo=True)


def conn():
    SQLModel.metadata.create_all(engine_url)


def get_session():
    with Session(engine_url) as session:
        yield session
