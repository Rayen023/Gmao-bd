from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Equipement, Panne
from django.core import serializers
from django.db.models import Count, Q

# Create your views here.


class EquipementList(ListView):
    model = Equipement
    context_object_name = 'Equipements'
    # model = Task
    # template_name = 'base/tasks.html' par deafaut : Task_list.html
    # context_object_name = 'tasks'
    # paginate_by = 5
    # ordering = ['-date_created']


class EquipementDetail(DetailView):
    model = Equipement
    context_object_name = 'Equipement'
    template_name = 'bd/Equipement.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['all_fiedls'] = serializers.serialize(
            "python", Equipement.objects.filter(pk=self.kwargs.get('pk')))
        context['Pannes'] = serializers.serialize(
            "python", Panne.objects.filter(id_equipement=self.kwargs.get('pk')))
        context['cPannes'] = Panne.objects.filter(
            id_equipement=self.kwargs.get('pk')).count()
        return context


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
