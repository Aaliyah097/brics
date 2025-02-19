from django.db import models
from django.contrib.postgres.search import SearchVectorField, SearchVector
from django.contrib.postgres.indexes import GinIndex
from django.db.models.signals import pre_save
from django.dispatch import receiver
from bricsid.fields import ULIDField
from users.models import User


class Organizations(models.Model):
    class StatusChoices(models.TextChoices):
        NEW = 'new', 'Новая'
        APPROVED = 'approved', 'Одобрена'
        REJECTED = 'rejected', 'Отклонена'

    id = ULIDField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    name = models.CharField(unique=True, max_length=64)
    short_name = models.CharField(unique=True, max_length=32)
    country = models.CharField(max_length=16)
    city = models.CharField(max_length=16)
    idx_number = models.CharField(max_length=128)

    contact_first_name = models.CharField(max_length=16)
    contact_last_name = models.CharField(max_length=16)
    contact_middle_name = models.CharField(max_length=16)

    ceo_first_name = models.CharField(max_length=16)
    ceo_last_name = models.CharField(max_length=16)
    ceo_middle_name = models.CharField(max_length=16)

    activity = models.CharField(max_length=128)
    email = models.EmailField(max_length=32)
    phone = models.CharField(max_length=16)
    contact_phone = models.CharField(max_length=16)
    
    status = models.CharField(
        max_length=16, 
        choices=StatusChoices.choices,
        default=StatusChoices.NEW
    )
    comment = models.TextField(default=None)

    search_vector = SearchVectorField(null=True)

    members = models.ManyToManyField(to=User, blank=True)

    class Meta:
        indexes = [
            GinIndex(fields=['search_vector']),
        ]


@receiver(pre_save, sender=Organizations)
def update_organizations_search_vector(sender, instance, **kwargs):
    if not instance.created_at:
        return
    instance.search_vector = SearchVector('short_name', 'name')
