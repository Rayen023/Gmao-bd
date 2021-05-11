# Generated by Django 3.1.6 on 2021-05-09 13:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0037_auto_20210509_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnel_maintenance',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]