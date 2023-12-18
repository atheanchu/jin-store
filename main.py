from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from routers.users import user_router
from routers.items import item_router
from routers.orders import order_router
from utils.load_data import initialize_users, initialize_items
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from utils.database import conn
from models import User, Item, Order

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


# Initialize tables


app.include_router(user_router)
app.include_router(item_router)
app.include_router(order_router)


@app.on_event("startup")
async def on_startup():
    conn()
    await initialize_users()
    await initialize_items()


@app.get("/")
async def index():
    return RedirectResponse(url="/items/")
