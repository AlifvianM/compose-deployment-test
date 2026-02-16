from typing import Annotated, Text
from fastapi import APIRouter, Path, Query, Request, status

from app.order.services import OrdersService
from app.order.repositories import OrdersRepository
from app.order.schemas import OrderRequest
from app.database.database import DBConnection

order_router = APIRouter(
    prefix="/api/v1/orders",
    tags=["orders"],
)

@order_router.get("/")
async def get_orders(
        db: DBConnection,
        request: Request,
    ):
    orders_service = OrdersService(orders_repository=OrdersRepository())
    orders = await orders_service.get_orders(conn=db)
    results = [order for order in orders]
    return results

@order_router.post("/create-order")
async def create_order(
        db: DBConnection,
        request: Request,
        params: OrderRequest
    ):
    orders_service = OrdersService(orders_repository=OrdersRepository())
    order = await orders_service.create_order(conn=db, params=params)
    return order