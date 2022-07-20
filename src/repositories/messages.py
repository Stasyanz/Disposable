import uuid

from fastapi.templating import Jinja2Templates

from src.repositories.base import BaseRepository
from src.db.messages import messages
from src.models.messages import Message, MessageOut
from src.core.services import create_link

templates = Jinja2Templates(directory="templates")


class MessageRepository(BaseRepository):

    async def main_page(self):
        return templates.TemplateResponse("index.html", context={"request": {}})

    async def get_by_id(self, id_: str):
        query = messages.select().where(messages.c.id == id_)
        message = await self.database.fetch_one(query)
        del_query = messages.delete().where(messages.c.id == id_)
        await self.database.fetch_one(del_query)
        text = None
        if message:
            text = Message.parse_obj(message).text
        return templates.TemplateResponse("message.html",
                                          context={
                                              "request": {},
                                              "text": text})

    async def create(self, new_message: Message):
        """Create a new Message"""

        values = {**new_message.dict(), 'id': str(uuid.uuid4())}
        message = MessageOut(**values)
        query = messages.insert().values(**values)
        await self.database.execute(query)
        link = create_link(message.id)
        return templates.TemplateResponse("created.html", context={"request": {}, "link": link})
