from django.db import models
from .equipement import Equipement
from .intervention import Intervention


class Gamme(models.Model):
    id_gamme = models.AutoField(primary_key=True, unique=True)
    Designation_Operation = models.CharField(max_length=200, blank=True)
    Frequence_Operation = models.CharField(max_length=50, blank=True)
    Duree_prevue_operation = models.CharField(max_length=50, blank=True)
    Mode_Operatoire = models.CharField(max_length=50, blank=True)

    id_equipement = models.ForeignKey(
        Equipement, on_delete=models.SET_NULL, null=True, blank=True)
    id_intervention = models.ForeignKey(
        Intervention, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        # in string fomat an equipement class takes its code
        return self.Designation_Operation

    class Meta:
        ordering = ['Designation_Operation']  # order equipements by Code_equip

    PREVENTIVE = 'P'
    CURATIVE = 'C'
    AMELIORATIVE = 'A'
    TYPE_OPERATION = [
        (PREVENTIVE, 'Preventive'),
        (CURATIVE, 'Curative'),
        (AMELIORATIVE, 'Ameliorative'),
    ]
    Type_Operation = models.CharField(
        max_length=2,
        choices=TYPE_OPERATION,
        default=PREVENTIVE,
    )
