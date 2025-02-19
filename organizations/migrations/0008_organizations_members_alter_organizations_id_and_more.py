# Generated by Django 5.1.5 on 2025-02-18 15:07

import bricsid.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0007_alter_organizations_id_organizationsmembers'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='organizations',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='organizations',
            name='id',
            field=bricsid.fields.ULIDField(default=bricsid.fields.ULIDField.generate_ulid, editable=False, max_length=26, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='OrganizationsMembers',
        ),
    ]
