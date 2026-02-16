from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy import RowMapping, select

from app.order.models import orders
from app.order.schemas import OrderRequest


class OrdersRepository:
    async def get_orders(
        self, 
        conn: AsyncConnection
    ) -> Sequence[RowMapping]:
        stmt = select(
            orders.c.id,
            orders.c.user_id,
            orders.c.product_id,
            orders.c.quantity,
            orders.c.status,
            orders.c.created_at,
            orders.c.updated_at,
        )
        try:
            result = await conn.execute(stmt)
            return result.mappings().fetchall()
        except Exception as e:
            raise Exception(e)
        
    async def create_order(
        self, 
        conn: AsyncConnection,
        params: OrderRequest
    ) -> RowMapping:
        stmt = orders.insert().values(
            user_id=params.user_id,
            product_id=params.product_id,
            quantity=params.quantity,
            status=params.status,
        ).returning(
            orders.c.id,
            orders.c.user_id,
            orders.c.product_id,
            orders.c.quantity,
            orders.c.status,
            orders.c.created_at,
            orders.c.updated_at,
        )
        try:
            result = await conn.execute(stmt)
            await conn.commit()
            return result.mappings().first()
        except Exception as e:
            await conn.rollback()
            raise Exception(e)