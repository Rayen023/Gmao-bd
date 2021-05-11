from django.contrib import admin
from .models import Equipement, Fournisseur, Intervention, Panne, PiecesR, Rechange, Documentation, Gamme, Emplacement, Outillages, Personnel_Maintenance, Etat_Intervention, Type_Intervention, KPI, Vals_KPI, Decisions_Amelioration


class EquipementInline(admin.TabularInline):
    model = Equipement
    extra = 0


class InterventionInline(admin.TabularInline):
    model = Intervention
    extra = 0


class PanneInline(admin.TabularInline):
    model = Panne
    extra = 0


class GammeInline(admin.TabularInline):
    model = Gamme
    extra = 0


class RechangeInline(admin.TabularInline):
    model = Rechange
    extra = 0


class InterventionAdmin(admin.ModelAdmin):
    model = Intervention
    inlines = [RechangeInline]


class EquipementAdmin(admin.ModelAdmin):
    Model = Equipement
    inlines = [PanneInline, GammeInline]


class PiecesRInline(admin.TabularInline):
    model = PiecesR
    extra = 0


class FournisseurAdmin(admin.ModelAdmin):
    model = Fournisseur
    inlines = [EquipementInline, PiecesRInline]


class EmplacementAdmin(admin.ModelAdmin):
    model = Emplacement
    inlines = [EquipementInline]


# Register your models here.
admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Equipement, EquipementAdmin)
admin.site.register(PiecesR)
admin.site.register(Panne)
admin.site.register(Documentation)
admin.site.register(Emplacement, EmplacementAdmin)
admin.site.register(Intervention, InterventionAdmin)
admin.site.register(Gamme)
admin.site.register(Personnel_Maintenance)
admin.site.register(Outillages)
admin.site.register(Etat_Intervention)
admin.site.register(Type_Intervention)
admin.site.register(KPI)
admin.site.register(Vals_KPI)
admin.site.register(Decisions_Amelioration)
