from users.models import User

def get_user_by_email(email: str) -> User | None:
    try:
        return User.objects.get(email=email)
    except User.DoesNotExist:
        return None
