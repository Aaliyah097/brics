# Generated by Django 5.1.5 on 2025-02-12 15:07

import bricsid.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0005_alter_organizations_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizations',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='organizations',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='organizations',
            name='id',
            field=bricsid.fields.ULIDField(default=bricsid.fields.ULIDField.generate_ulid, editable=False, max_length=26, primary_key=True, serialize=False),
        ),
    ]
