from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Equipement(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    Code_Equip = models.IntegerField(primary_key=True, unique=True, blank=True)
    Designation = models.TextField(max_length=200, blank=True)
    Date_Ach = models.DateTimeField(auto_now_add=True, blank=True)
    Date_mise_service = models.DateTimeField(auto_now_add=True, blank=True)
    Carct_tech = models.CharField(max_length=300, blank=True)
    Date_fin_garantie = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.Designation  # in string fomat an equipement class takes its code

    class Meta:
        ordering = ['Code_Equip']  # order equipements by Code_equip
