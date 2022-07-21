from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse


from src.repositories.messages import MessageRepository
from src.models.messages import Message
from src.endpoints.depends import get_message_repository

router = APIRouter()


@router.get("/{msg_id}", response_class=HTMLResponse, tags=['Messages'])
async def read_message_by_id(
        msg_id: str,
        messages: MessageRepository = Depends(get_message_repository),
        ):
    return await messages.get_by_id(msg_id)


@router.post("/", response_class=HTMLResponse, tags=['Messages'])
async def create_message(
        request: Request,
        messages: MessageRepository = Depends(get_message_repository)):
    message = Message(**await request.form())
    return await messages.create(new_message=message)

