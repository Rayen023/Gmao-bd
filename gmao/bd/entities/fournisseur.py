from django.db import models


class Fournisseur(models.Model):
    id_fournisseur = models.IntegerField(primary_key=True, unique=True)
    Designation_fournisseur = models.CharField(max_length=200, blank=True)

    def __str__(self):
        # in string fomat an equipement class takes its code
        return self.Designation_fournisseur

    class Meta:
        ordering = ['id_fournisseur']  # order equipements by Code_equip
