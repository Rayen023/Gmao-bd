# Generated by Django 3.1.6 on 2021-05-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0020_auto_20210508_1619'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='panne',
            options={'ordering': ['Description_Panne']},
        ),
        migrations.AddField(
            model_name='panne',
            name='Description_Panne',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]