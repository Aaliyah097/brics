from django.core.mail import send_mail
from config import config


def send_signup_email(email: str, nonce: str):
    send_mail(
        "Завершение регистрации", 
        f"Привет! Твой код для завершения регистрациии -> {nonce} !", 
        config.EMAIL_SENDER,
        [email]
    )
