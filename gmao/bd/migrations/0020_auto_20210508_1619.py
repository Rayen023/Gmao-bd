# Generated by Django 3.1.6 on 2021-05-08 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0019_auto_20210508_1613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='intervention',
            options={'ordering': ['Designation_Intervention']},
        ),
        migrations.AddField(
            model_name='intervention',
            name='Designation_Intervention',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]