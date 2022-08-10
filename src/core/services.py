from secrets import token_urlsafe

from src.core.config import fqdn, schema, config


def create_link(message_id: str):
    return f"{schema}{fqdn}:{config.get('SERVER_PORT')}/{message_id}"


def generate_id():
    """Generate message.id"""
    return token_urlsafe(64)
