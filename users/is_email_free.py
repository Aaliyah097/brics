from users.models import User
from django.core.cache import cache


def is_email_free(email: str) -> bool:
    if cache.get(email):
        return False

    try:
        _ = User.objects.get(email=email)
        return False
    except User.DoesNotExist:
        return True
