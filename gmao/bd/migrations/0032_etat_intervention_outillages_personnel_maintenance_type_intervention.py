# Generated by Django 3.1.6 on 2021-05-08 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0031_auto_20210509_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etat_Intervention',
            fields=[
                ('Id_Etat_Intervention', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Designation_Etat_Intervention', models.CharField(choices=[('Programmee', 'Programmee'), ('Encours', 'Encours'), ('Realisee', 'Realisee'), ('Annulee', 'Annulee')], default='Programmee', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Outillages',
            fields=[
                ('Id_Outillage', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Code_Outillage', models.IntegerField(blank=True, null=True)),
                ('Designation_Outillage', models.CharField(blank=True, max_length=200)),
                ('Photo_Outillage', models.ImageField(blank=True, null=True, upload_to='')),
                ('Caracteristique_Techniques_Outillage', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel_Maintenance',
            fields=[
                ('Id_Personnel', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Matricule_Personnel', models.IntegerField(blank=True, null=True)),
                ('Nom', models.CharField(blank=True, max_length=200)),
                ('Prenom', models.CharField(blank=True, max_length=200)),
                ('Tel', models.IntegerField(blank=True, null=True)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Qualifications', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Type_Intervention',
            fields=[
                ('Id_Type_Intervention', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Type_Intervention', models.CharField(choices=[('P', 'Preventive'), ('C', 'Curative')], default='P', max_length=2)),
            ],
        ),
    ]
