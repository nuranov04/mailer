from fastapi_mail import ConnectionConfig
from decouple import config


class EmailConf:
    MAIL_USERNAME = config("MAIL_USERNAME")
    MAIL_PASSWORD = config("MAIL_PASSWORD")
    MAIL_FROM = config("MAIL_FROM")
    MAIL_PORT = config("MAIL_PORT")
    MAIL_SERVER = config("MAIL_SERVER")
    MAIL_FROM_NAME = config("MAIL_FROM_NAME")
    MAIL_STARTTLS = config("MAIL_STARTTLS")
    MAIL_TLS = config("MAIL_TLS")
    MAIL_SSL = config("MAIL_SSL")
    MAIL_SSL_TLS = config("MAIL_SSL_TLS")
    USE_CREDENTIALS = config("USE_CREDENTIALS")
    VALIDATE_CERTS = config("VALIDATE_CERTS")

    def get_conf(self):
        return ConnectionConfig(
            MAIL_USERNAME=self.MAIL_FROM,
            MAIL_PASSWORD=self.MAIL_PASSWORD,
            MAIL_PORT=self.MAIL_PORT,
            MAIL_SERVER=self.MAIL_SERVER,
            MAIL_STARTTLS=self.MAIL_STARTTLS,
            MAIL_SSL_TLS=self.MAIL_SSL_TLS,
            MAIL_FROM=self.MAIL_FROM
        )


email_conf = EmailConf()
