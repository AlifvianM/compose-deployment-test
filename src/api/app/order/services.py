from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy import RowMapping

from app.order.repositories import OrdersRepository
from app.order.schemas import OrderRequest


class OrdersService:
    def __init__(
            self, 
            orders_repository: OrdersRepository,
            # params: OrderRequest
        ):
        self.orders_repository = orders_repository
        # self.params = params

    async def get_orders(
            self, 
            conn: AsyncConnection
        ) -> Sequence[RowMapping]:
        result = await self.orders_repository.get_orders(conn)
        return result
    
    async def create_order(
            self, 
            conn: AsyncConnection,
            params: OrderRequest
        ) -> RowMapping:
        result = await self.orders_repository.create_order(conn, params=params)
        return result