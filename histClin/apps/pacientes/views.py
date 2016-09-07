from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.pacientes.forms import PacienteForm
from apps.pacientes.models import Paciente
from django.views.generic import ListView,CreateView,UpdateView
from django.core.urlresolvers import reverse_lazy
#Instalar para campo de formulario con fecha
#https://github.com/nkunihiko/django-bootstrap3-datetimepicker

def index(request):
    return render(request, 'paciente/index.html')


class paciente_view(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/paciente_form.html'
    success_url = reverse_lazy('paciente:paciente_listar')
    
   

class paciente_list(ListView):
    model = Paciente
    template_name = 'pacientes/paciente_list.html'
    success_url = reverse_lazy('paciente:paciente_listar')
    
class paciente_edit(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/paciente_form.html'
    success_url = reverse_lazy('paciente:paciente_listar')
    
class paciente_delete(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/paciente_delete.html'
    success_url = reverse_lazy('paciente:paciente_listar')