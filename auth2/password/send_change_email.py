from bricsid.send_email import send_mail
from config import config


def send_change_email(email: str, nonce: str):
    send_mail(
        "Подтверждение смены пароля", 
        f"Привет! Твой код для смены пароля -> {nonce} !", 
        config.EMAIL_SENDER, 
        [email]
    )
