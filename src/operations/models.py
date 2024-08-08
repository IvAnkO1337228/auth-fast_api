from sqlalchemy import Column, Integer, String, Table, MetaData


metadata = MetaData()

book = Table(
    "book",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("author", String, nullable=False),
    Column("category", String, nullable=False),
    Column("year", Integer, nullable=False),
)