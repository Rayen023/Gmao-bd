from django.db import models
from django.contrib.auth.models import User
from .fournisseur import Fournisseur


class Documentation(models.Model):
    id_Document = models.AutoField(primary_key=True)
    Code_Document = models.IntegerField(blank=True, null=True)
    Designation_doc = models.CharField(max_length=200, blank=True)
    Lien_fichier_joint = models.URLField(blank=True, null=True)

    def __str__(self):
        # in string fomat an equipement class takes its code
        return self.Designation_doc


class Emplacement(models.Model):
    id_Emplacement = models.AutoField(primary_key=True)
    Designation_Emplacement = models.CharField(max_length=200, blank=True)

    def __str__(self):
        # in string fomat an equipement class takes its code
        return self.Designation_Emplacement

    class Meta:
        # order equipements by Code_equip
        ordering = ['Designation_Emplacement']


class Equipement(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    Code_Equip = models.AutoField(primary_key=True)
    Designation = models.CharField(max_length=200, blank=True)
    Date_Ach = models.DateTimeField(auto_now_add=True, blank=True)
    Date_mise_service = models.DateTimeField(auto_now_add=True, blank=True)
    Carct_tech = models.CharField(max_length=300, blank=True)
    Date_fin_garantie = models.DateTimeField(blank=True)
    Photo_Equip = models.ImageField(null=True, blank=True)
    # Photo_Equip = models.ImageField(upload_to='images', blank=True)
    id_Document = models.OneToOneField(
        Documentation, on_delete=models.CASCADE, null=True, blank=True)
    id_fournisseur = models.ForeignKey(
        Fournisseur, on_delete=models.SET_NULL, null=True, blank=True)
    id_Emplacement = models.ForeignKey(
        Emplacement, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.Designation  # in string fomat an equipement class takes its code

    class Meta:
        ordering = ['Code_Equip']  # order equipements by Code_equip
