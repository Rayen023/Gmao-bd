from django.contrib import admin
from .models import Equipement, Fournisseur, Intervention, Panne, PiecesR, Rechange, Documentation
# Register your models here.


class EquipementInline(admin.TabularInline):
    model = Equipement
    extra = 1


class PiecesRInline(admin.TabularInline):
    model = PiecesR
    extra = 1


class RechangeInline(admin.TabularInline):
    model = Rechange
    extra = 1


class InterventionInline(admin.TabularInline):
    model = Intervention
    extra = 1


class PanneInline(admin.TabularInline):
    model = Panne
    extra = 1


class FournisseurAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['Designation_fournisseur']})]
    inlines = [EquipementInline, PiecesRInline]


class InterventionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['id_intervention']})]
    inlines = [RechangeInline]


class EquipementAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['Designation']}),
                 (None, {'fields': ['Code_Equip']}), (None, {'fields': ['id_Document']})]
    inlines = [PanneInline]


admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Equipement, EquipementAdmin)
admin.site.register(PiecesR)
admin.site.register(Panne)
admin.site.register(Documentation)
admin.site.register(Intervention, InterventionAdmin)
