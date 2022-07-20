from pydantic import BaseModel


class Config:
    arbitrary_types_allowed = True


class Message(BaseModel):
    text: str = ""


class MessageOut(Message):
    id: str
