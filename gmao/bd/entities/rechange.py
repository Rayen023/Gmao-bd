from django.db import models
from .pieceR import PiecesR
from .intervention import Intervention


class Rechange(models.Model):
    id_intervention = models.ForeignKey(
        Intervention, on_delete=models.SET_NULL, null=True, blank=True)
    id_pieceR = models.ForeignKey(
        PiecesR, on_delete=models.SET_NULL, null=True, blank=True)
