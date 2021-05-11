from django.db import models
from .entities.equipement import Equipement, Documentation, Emplacement
from .entities.fournisseur import Fournisseur
from .entities.intervention import Intervention, Outillages, Type_Intervention, Personnel_Maintenance, Etat_Intervention
from .entities.panne import Panne
from .entities.gamme import Gamme
from .entities.pieceR import PiecesR
from .entities.rechange import Rechange
from .entities.kpi import KPI, Vals_KPI, Decisions_Amelioration

# Create your models here.
