# models.py
from sqlalchemy import Table, Column, Integer, String
from database import metadata

schoolHouse = Table(
    "schoolHouse",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("count", Integer, index=True),
    Column("name", String, index=True),
)


