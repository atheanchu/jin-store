from fastapi import APIRouter, Depends, Request
from sqlmodel import Session
from utils.database import get_session
from models import Item
from . import templates

item_router = APIRouter(prefix="/items")


@item_router.get("/")
async def get_items(request: Request, db: Session = Depends(get_session)):
    items = db.query(Item).order_by(Item.id.asc()).all()

    db.close()
    return templates.TemplateResponse("item.html", {"request": request, "items": items})
    # return items
