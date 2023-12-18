from fastapi import APIRouter, Depends, Request
from sqlmodel import Session, select
from models import Order, OrderCreate, OrderRead, Item
from utils.database import get_session
from datetime import datetime
from typing import List
from fastapi.responses import HTMLResponse
from . import templates

order_router = APIRouter(prefix="/orders")


@order_router.post("/", response_model=OrderCreate)
async def create_new_order(
    request: Request, order: OrderCreate, db: Session = Depends(get_session)
):
    new_order = Order(username=order.username, item_id=order.item_id, order_date=datetime.now())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


@order_router.get("/")
async def get_orders(request: Request, db: Session = Depends(get_session)):
    # Get all orders from the database
    results = db.query(Order).all()
    orders = list()

    for order in results:
        query = select(Item).where(Item.id == order.item_id)
        item = db.exec(query).first()

        temp_order = OrderRead(
            id=order.id,
            username=order.username,
            order_date=order.order_date,
            item_name=item.name,
        )
        orders.append(temp_order)

    return templates.TemplateResponse("order.html", {"request": request, "orders": orders})
    # return results
