import uuid

from sqlalchemy import Column, Integer, String, Table, UUID, DateTime
from sqlalchemy.sql import func

from app.models.base import get_audit_columns
from app.database.client import metadata

orders = Table(
    "order",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("user_id", Integer, nullable=False),
    Column("product_id", Integer, nullable=False),
    Column("quantity", Integer, nullable=False),
    Column("status", String(50), nullable=False),
    Column("created_at", DateTime(timezone=True), nullable=False, server_default=func.now()),
    Column("updated_at", DateTime(timezone=True), nullable=True),
    # *get_audit_columns(),
)