from starlette.responses import JSONResponse
from fastapi import Depends, HTTPException, APIRouter

from typing import Any, List
from app.services import email_service
from app.models import mail
from utils.logger import logger

router = APIRouter()


@router.post("/send_email")
async def send_email(body: mail.MessageSchema) -> JSONResponse:
    logger.info(f"request in send_email. body == {body}")
    if not body.check_subject() or not body.check_message():
        logger.info(f"not subject and message validate. They are empty")
        return JSONResponse(
            status_code=400,
            content={"error": "subject and message must be not empty"}
        )
    bode_dict = body.dict()
    await email_service.send_message(to=bode_dict.get("to"),
                                     subject=bode_dict.get("subject"),
                                     message=bode_dict.get("message"))
    return JSONResponse(
        status_code=200, content={"status": "done"}
    )
