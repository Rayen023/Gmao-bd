from django.urls import path
from .views import EquipementDelete, EquipementList, EquipementDetail, EquipementCreate, EquipementUpdate

urlpatterns = [
    path('', EquipementList.as_view(), name='Equipements'),
    path('Equipement/<int:pk>/', EquipementDetail.as_view(), name='Equipement'),
    path('Equipement-create/', EquipementCreate.as_view(),
         name='Equipement-create'),
    path('Equipement-update/<int:pk>/',
         EquipementUpdate.as_view(), name='Equipement-update'),
    path('Equipement-delete/<int:pk>/', EquipementDelete.as_view(), name='Equipement-delete'), ]
