from src.db.messages import messages
from src.db.base import metadata, engine


metadata.create_all(bind=engine)
