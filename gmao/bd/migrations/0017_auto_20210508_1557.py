# Generated by Django 3.1.6 on 2021-05-08 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0016_auto_20210508_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipement',
            name='Code_Equip',
            field=models.AutoField(default=3, primary_key=True, serialize=False, unique=True),
        ),
    ]
