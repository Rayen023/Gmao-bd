from django.db import models
from .fournisseur import Fournisseur


class PiecesR(models.Model):
    id_pieceR = models.AutoField(primary_key=True, unique=True)
    Designation_piece_Rechange = models.CharField(max_length=200, blank=True)
    Code_Piece = models.IntegerField(null=True, blank=True)
    Quantite_Pieces_rechange = models.IntegerField(blank=True, null=True)

    id_fournisseur = models.ForeignKey(
        Fournisseur, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        # in string fomat an equipement class takes its code
        return self.Designation_piece_Rechange

    class Meta:
        # order equipements by Code_equip
        ordering = ['Designation_piece_Rechange']
