# Generated by Django 3.1.6 on 2021-05-09 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0032_etat_intervention_outillages_personnel_maintenance_type_intervention'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamme',
            name='Duree_prevue_operation',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='gamme',
            name='Frequence_Operation',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='gamme',
            name='Mode_Operatoire',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
