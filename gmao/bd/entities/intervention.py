from django.db import models
from django.core.validators import RegexValidator


class Personnel_Maintenance(models.Model):
    Id_Personnel = models.AutoField(primary_key=True, unique=True)
    Matricule_Personnel = models.IntegerField(null=True, blank=True)
    Nom = models.CharField(max_length=200, blank=True)
    Prenom = models.CharField(max_length=200, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Qualifications = models.CharField(max_length=200, blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Tel = models.CharField(
        validators=[phone_regex], max_length=17, null=True, blank=True)  # validators should be a list


class Outillages(models.Model):
    Id_Outillage = models.AutoField(primary_key=True, unique=True)
    Code_Outillage = models.IntegerField(null=True, blank=True)
    Designation_Outillage = models.CharField(max_length=200, blank=True)
    Photo_Outillage = models.ImageField(null=True, blank=True)
    Caracteristique_Techniques_Outillage = models.CharField(
        max_length=200, blank=True)


class Type_Intervention(models.Model):
    Id_Type_Intervention = models.AutoField(primary_key=True, unique=True)

    PREVENTIVE = 'P'
    CURATIVE = 'C'
    TYPE_INTERVENTION = [
        (PREVENTIVE, 'Preventive'),
        (CURATIVE, 'Curative'),
    ]
    Type_Intervention = models.CharField(
        max_length=2,
        choices=TYPE_INTERVENTION,
        default=PREVENTIVE,
    )


class Etat_Intervention(models.Model):
    Id_Etat_Intervention = models.AutoField(primary_key=True, unique=True)
    PROGRAMEE = 'Programmee'
    ENCOURS = 'Encours'
    REALISEE = 'Realisee'
    ANNULEE = 'Annulee'
    DESIGNATION_INTERVENTION = [
        (PROGRAMEE, 'Programmee'),
        (ENCOURS, 'Encours'),
        (REALISEE, 'Realisee'),
        (ANNULEE, 'Annulee'),
    ]
    Designation_Etat_Intervention = models.CharField(
        max_length=10,
        choices=DESIGNATION_INTERVENTION,
        default=PROGRAMEE,
    )


class Intervention(models.Model):
    id_intervention = models.AutoField(primary_key=True, unique=True)
    Designation_Intervention = models.CharField(max_length=200, blank=True)
    Code_Intervention = models.IntegerField(null=True, blank=True)
    Date_deb_prevue_Intervention = models.DateTimeField(
        null=True, auto_now_add=True)
    Date_Fin_prevue_Intervention = models.DateTimeField(null=True, blank=True)
    Date_deb_Reelle_Intervention = models.DateTimeField(
        null=True,  auto_now_add=True)
    Date_Fin_Reelle_Intervention = models.DateTimeField(null=True, blank=True)
    Duree_prevue = models.DurationField(blank=True, null=True)
    Duree_Reelle = models.DurationField(blank=True, null=True)
    Id_Personnel = models.ForeignKey(
        Personnel_Maintenance, on_delete=models.SET_NULL, null=True, blank=True)
    Id_Outillage = models.ForeignKey(
        Outillages, on_delete=models.SET_NULL, null=True, blank=True)
    Id_Type_Intervention = models.ForeignKey(
        Type_Intervention, on_delete=models.SET_NULL, null=True, blank=True)
    Id_Etat_Intervention = models.ForeignKey(
        Etat_Intervention, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        # in string fomat an equipement class takes its code
        return self.Designation_Intervention

    class Meta:
        # order equipements by Code_equip
        ordering = ['Designation_Intervention']
