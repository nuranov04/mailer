from fastapi_mail import FastMail, MessageSchema, MessageType

from utils import email_conf, logger


async def send_message(*, to: str, subject: str, message: str):

    logger.logger.info(f"Sending message to {to} with subject=={subject} and with message=={message}")

    message = MessageSchema(
        subject=subject,
        recipients=[to],
        body=message,
        subtype=MessageType.plain
    )

    fm = FastMail(email_conf.email_conf.get_conf())
    await fm.send_message(message)

    logger.logger.info("message in sent")
