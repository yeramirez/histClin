from django.shortcuts import render
from django.http import HttpResponse
from apps.medico.models import Medico
from apps.medico.forms import MedicoForm
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class Medico_Crear(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico/medico_form.html'
    success_url = reverse_lazy('paciente:paciente_listar')

class Medico_list(ListView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico/medico_list.html'
    success_url = reverse_lazy('paciente:paciente_listar')
    
class Medico_edit(UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico/medico_profile.html'
    success_url = reverse_lazy('medico:medico_listar')
    
class Medico_delete(DeleteView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico/medico_delete.html'
    success_url = reverse_lazy('medico:medico_listar')