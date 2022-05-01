from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0028_auto_20210509_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipement',
            name='Date_fin_garantie',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='Adresse_Four',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='Civilite',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='Code_Fourn',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='Contact_principal',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='Email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='Site_web',
            field=models.URLField(blank=True),
        ),
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
        migrations.AddField(
            model_name='intervention',
            name='Code_Intervention',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intervention',
            name='Date_Fin_Reelle_Intervention',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intervention',
            name='Date_Fin_prevue_Intervention',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intervention',
            name='Date_deb_Reelle_Intervention',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='intervention',
            name='Date_deb_prevue_Intervention',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='intervention',
            name='Duree_Reelle',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intervention',
            name='Duree_prevue',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='panne',
            name='Code_Panne',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='panne',
            name='Date_H_Min_Declaration',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='panne',
            name='Declarant',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='panne',
            name='Duree_Reelle_Panne',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='piecesr',
            name='Code_Piece',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='piecesr',
            name='Quantite_Pieces_rechange',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='panne',
            name='Code_Panne',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='panne',
            name='Date_H_Min_Declaration',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='panne',
            name='Declarant',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='panne',
            name='Duree_Reelle_Panne',
            field=models.TimeField(blank=True, null=True),
        ),
    ]