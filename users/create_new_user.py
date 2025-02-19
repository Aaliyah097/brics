from users.models import User


def create_new_user(email: str, password: str) -> int:
    new_user = User(email=email)
    new_user.set_password(password)
    new_user.is_active = True
    new_user.save()
    new_user.refresh_from_db()

    return new_user.id
