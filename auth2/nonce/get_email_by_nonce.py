from django.core.cache import cache


def get_email_by_nonce(nonce: str) -> str | None:
    email = cache.get(nonce)
    if not email:
        return None
    cache.delete(email)
    cache.delete(nonce)

    return email
