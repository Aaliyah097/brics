# Generated by Django 5.1.6 on 2025-02-19 14:42

import bricsid.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0013_alter_organizations_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizations',
            name='id',
            field=bricsid.fields.ULIDField(default=bricsid.fields.ULIDField.generate_ulid, editable=False, max_length=26, primary_key=True, serialize=False),
        ),
    ]
