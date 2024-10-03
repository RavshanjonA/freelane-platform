# Generated by Django 5.1.1 on 2024-10-01 12:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_joblocation_jobannounce_owner_jobannounce_profession_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobannounce',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to=settings.AUTH_USER_MODEL),
        ),
    ]
