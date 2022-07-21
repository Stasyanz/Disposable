from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse


from src.repositories.messages import MessageRepository
from src.endpoints.depends import get_message_repository

router = APIRouter()


@router.get("/", response_class=HTMLResponse, tags=['index'])
async def main_page(
        messages: MessageRepository = Depends(get_message_repository),
        ):
    return await messages.main_page()
