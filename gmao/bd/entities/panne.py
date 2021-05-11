from django.db import models
from .equipement import Equipement
from .intervention import Intervention


class Panne(models.Model):
    id_panne = models.AutoField(primary_key=True, unique=True)
    Description_Panne = models.CharField(max_length=200, blank=True)
    Code_Panne = models.IntegerField(null=True, blank=True)
    Date_H_Min_Declaration = models.DateTimeField(
        auto_now_add=True, null=True)
    Declarant = models.CharField(max_length=100, blank=True)
    Duree_Reelle_Panne = models.TimeField(null=True, blank=True)

    id_equipement = models.ForeignKey(
        Equipement, on_delete=models.SET_NULL, null=True, blank=True)
    id_intervention = models.ForeignKey(
        Intervention, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        # in string fomat an equipement class takes its code
        return self.Description_Panne

    class Meta:
        ordering = ['Description_Panne']  # order equipements by Code_equip
