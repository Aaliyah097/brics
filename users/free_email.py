from users.models import User
from django.core.cache import cache


def free_email(email: str):
    cache.delete(email)

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return

    user.delete()
