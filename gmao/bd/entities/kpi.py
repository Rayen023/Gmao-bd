from django.db import models


class Vals_KPI(models.Model):
    id_Vals_KPIs = models.AutoField(primary_key=True, unique=True)
    Date_deb_Val_KPI = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    Date_fin_Val_KPI = models.DateTimeField(blank=True, null=True)
    Valeur_KPI = models.IntegerField(blank=True, null=True)
    Commentaires_Val_KPI = models.CharField(
        max_length=200, blank=True, null=True)

    def __str__(self):
        # in string fomat an equipement class takes its code
        return self.Commentaires_Val_KPI

    class Meta:
        ordering = ['Commentaires_Val_KPI']  # order equipements by Code_equip


class Decisions_Amelioration(models.Model):
    id_Decisions_Amelioration = models.AutoField(
        primary_key=True, unique=True)
    Code_action = models.IntegerField(blank=True, null=True)
    Designation_Action = models.CharField(
        max_length=200, blank=True, null=True)
    Date_deb = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    Date_Fin = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        # in string fomat an equipement class takes its code
        return self.Designation_Action

    class Meta:
        ordering = ['Designation_Action']  # order equipements by Code_equip


class KPI(models.Model):
    id_KPI = models.AutoField(primary_key=True, unique=True)
    Code_KPI = models.IntegerField(blank=True, null=True)
    Designation_KPI = models.CharField(
        max_length=200, blank=True, null=True)
    Frequence_Calcul_KPI = models.CharField(
        max_length=20, blank=True, null=True)
    Methode_Calcul_KPI = models.CharField(
        max_length=200, blank=True, null=True)
    id_Vals_KPIs = models.ForeignKey(
        Vals_KPI, on_delete=models.SET_NULL, null=True, blank=True)
    id_Decisions_Amelioration = models.ForeignKey(
        Decisions_Amelioration, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        # in string fomat an equipement class takes its code
        return self.Designation_KPI

    class Meta:
        ordering = ['Designation_KPI']  # order equipements by Code_equip
