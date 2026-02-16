from datetime import datetime

from pydantic import BaseModel


class OrderRequest(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    status: str
    created_at: datetime = datetime.now()
    updated_at: datetime