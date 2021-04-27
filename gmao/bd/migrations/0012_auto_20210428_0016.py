# Generated by Django 3.1.6 on 2021-04-27 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0011_documentation_designation_doc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentation',
            name='id_equipement',
        ),
        migrations.AddField(
            model_name='equipement',
            name='id_Document',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bd.documentation'),
        ),
    ]
