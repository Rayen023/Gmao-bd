# Generated by Django 3.1.6 on 2021-04-27 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0003_auto_20210419_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id_fournisseur', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Designation_fournisseur', models.TextField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ['id_fournisseur'],
            },
        ),
        migrations.AlterField(
            model_name='equipement',
            name='Code_Equip',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='equipement',
            name='id_fournisseur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bd.fournisseur'),
        ),
    ]
