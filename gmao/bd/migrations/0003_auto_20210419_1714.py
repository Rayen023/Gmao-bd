# Generated by Django 3.1.6 on 2021-04-19 15:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bd', '0002_auto_20210419_1655'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Equipements',
            new_name='Equipement',
        ),
    ]
