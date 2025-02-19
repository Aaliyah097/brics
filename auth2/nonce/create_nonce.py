import random


from django.core.cache import cache


def create_nonce(email: str) -> int:
    nonce = random.randint(10000000, 99999999)
    cache.set(nonce, email, timeout=60*15)
    cache.set(email, 1, timeout=60*15)
    return nonce
