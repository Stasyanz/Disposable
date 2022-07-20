from src.db.base import database
from src.repositories.messages import MessageRepository


def get_message_repository() -> MessageRepository:
    return MessageRepository(database)
