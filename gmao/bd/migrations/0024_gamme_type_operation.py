# Generated by Django 3.1.6 on 2021-05-08 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0023_auto_20210508_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamme',
            name='Type_Operation',
            field=models.CharField(choices=[('FR', 'Preventive'), ('SO', 'Curative'), ('JR', 'Ameliorative')], default='FR', max_length=2),
        ),
    ]
