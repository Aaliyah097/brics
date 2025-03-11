from bricsid.send_email import send_mail
from config import config


def send_2fa_email(email: str, nonce: str):
    send_mail(
        "Подтверждение входа", 
        f"Привет! Твой код для входа -> {nonce} !", 
        config.EMAIL_SENDER, 
        [email]
    )
