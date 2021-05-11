from django.db import models


class Fournisseur(models.Model):
    id_fournisseur = models.AutoField(primary_key=True, unique=True)
    Designation_fournisseur = models.CharField(max_length=200, blank=True)
    Code_Fourn = models.IntegerField(blank=True, null=True)
    Adresse_Four = models.CharField(max_length=200, blank=True)
    Civilite = models.CharField(max_length=100, blank=True)
    Site_web = models.URLField(blank=True)
    Email = models.EmailField(blank=True)
    Contact_principal = models.CharField(max_length=200, blank=True)

    def __str__(self):
        # in string fomat an equipement class takes its code
        return self.Designation_fournisseur

    class Meta:
        ordering = ['id_fournisseur']  # order equipements by Code_equip
