from pydantic import BaseModel, EmailStr


class MessageSchema(BaseModel):
    to: EmailStr
    subject: str
    message: str

    def check_subject(self):
        if self.subject == "":
            return False
        return True

    def check_message(self):
        if self.message == "":
            return False
        return True
