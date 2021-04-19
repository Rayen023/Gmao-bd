from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Equipement
# Create your views here.


class EquipementList(ListView):
    model = Equipement
    context_object_name = 'Equipements'


class EquipementDetail(DetailView):
    model = Equipement
    context_object_name = 'Equipement'
    template_name = 'bd/Equipement.html'


class EquipementCreate(CreateView):
    model = Equipement
    fields = '__all__'  # all items in the class
    success_url = reverse_lazy('Equipements')


class EquipementUpdate(UpdateView):
    model = Equipement
    fields = '__all__'  # all items in the class
    success_url = reverse_lazy('Equipements')


class EquipementDelete(DeleteView):
    model = Equipement
    context_object_name = 'Equipement'
    success_url = reverse_lazy('Equipements')
