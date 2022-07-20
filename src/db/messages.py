import sqlalchemy

from src.db.base import metadata

messages = sqlalchemy.Table(
    "messages",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True, autoincrement=False, unique=True),
    sqlalchemy.Column("link", sqlalchemy.String),
    sqlalchemy.Column("viewed", sqlalchemy.Boolean),
    sqlalchemy.Column("delete_at", sqlalchemy.Integer),
    sqlalchemy.Column("text", sqlalchemy.String),
)

