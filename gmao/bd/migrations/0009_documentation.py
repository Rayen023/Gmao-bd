# Generated by Django 3.1.6 on 2021-04-27 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0008_auto_20210427_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id_Document', models.IntegerField(primary_key=True, serialize=False)),
                ('id_equipement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bd.equipement')),
            ],
        ),
    ]
