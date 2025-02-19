from typing import Any
from organizations.models import Organizations
from users.models import User
from django.db import transaction


def create_organization(organization: dict[str, Any], user_id: int) -> int | None:
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None

    name = organization['name']
    short_name = organization['short_name']
    del organization['members']

    ex_organizations = Organizations.objects.filter(
        name__iexact=name,
        short_name__iexact=short_name
    ).count()

    if ex_organizations:
        return None
    
    with transaction.atomic():
        new_org = Organizations.objects.create(**organization)
        new_org.members.add(user)
        new_org.save()

    return new_org.id
