from django.db import models
from django.contrib.auth.models import User
from .entities.fournisseur import Fournisseur
# Create your models here.


class Documentation(models.Model):
    id_Document = models.IntegerField(primary_key=True)
    Designation_doc = models.CharField(max_length=200, blank=True)

    def __str__(self):
        # in string fomat an equipement class takes its code
        return self.Designation_doc


class Equipement(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    Code_Equip = models.IntegerField(primary_key=True, unique=True)
    Designation = models.CharField(max_length=200, blank=True)
    Date_Ach = models.DateTimeField(auto_now_add=True, blank=True)
    Date_mise_service = models.DateTimeField(auto_now_add=True, blank=True)
    Carct_tech = models.CharField(max_length=300, blank=True)
    Date_fin_garantie = models.DateTimeField(auto_now_add=True, blank=True)
    id_Document = models.OneToOneField(
        Documentation, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.Designation  # in string fomat an equipement class takes its code

    class Meta:
        ordering = ['Code_Equip']  # order equipements by Code_equip

    id_fournisseur = models.ForeignKey(
        Fournisseur, on_delete=models.SET_NULL, null=True, blank=True)


class Intervention(models.Model):
    id_intervention = models.IntegerField(primary_key=True, unique=True)

    # def __str__(self):
    #     # in string fomat an equipement class takes its code
    #     return self.id_intervention

    # class Meta:
    #     ordering = ['id_intervention']  # order equipements by Code_equip


class Panne(models.Model):
    id_panne = models.IntegerField(primary_key=True, unique=True)
    id_equipement = models.ForeignKey(
        Equipement, on_delete=models.SET_NULL, null=True, blank=True)
    id_intervention = models.ForeignKey(
        Intervention, on_delete=models.SET_NULL, null=True, blank=True)

    # def __str__(self):
    #     # in string fomat an equipement class takes its code
    #     return self.id_panne

    # class Meta:
    #     ordering = ['id_panne']  # order equipements by Code_equip


class PiecesR(models.Model):
    id_pieceR = models.IntegerField(primary_key=True, unique=True)
    id_fournisseur = models.ForeignKey(
        Fournisseur, on_delete=models.SET_NULL, null=True, blank=True)

    # def __str__(self):
    #     # in string fomat an equipement class takes its code
    #     return self.id_pieceR

    # class Meta:
    #     ordering = ['id_pieceR']  # order equipements by Code_equip


class Rechange(models.Model):
    id_intervention = models.ForeignKey(
        Intervention, on_delete=models.SET_NULL, null=True, blank=True)
    id_pieceR = models.ForeignKey(
        PiecesR, on_delete=models.SET_NULL, null=True, blank=True)
