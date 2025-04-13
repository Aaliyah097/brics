from config import config
from django.core.mail import send_mail as django_send_email
import os
import ssl
import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage


def send_mail(theme: str,  message: str, sender: str, email: str):
    if config.DEBUG:
        django_send_email(theme, message, sender or config.EMAIL_SENDER, email)
    else:
        msg = EmailMessage()
        msg['From'] = config.EMAIL_SENDER
        msg['To'] = [email]
        msg['Subject'] = theme

        msg.set_content(message)

        with smtplib.SMTP(
            config.EMAIL_HOST, 
            config.EMAIL_PORT,
            local_hostname='0.0.0.0'
        ) as connection:
            connection.starttls()
            connection.login(
                config.EMAIL_HOST_DOMAIN + "\\" + config.EMAIL_HOST_USER, 
                config.EMAIL_HOST_PASSWORD
            )
            connection.send_message(msg)
