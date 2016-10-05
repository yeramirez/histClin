from django.shortcuts import render
from django.http import HttpResponse
from apps.medico.models import Medico
from apps.medico.forms import MedicoForm
from django.views.generic import ListView,CreateView,UpdateView
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class Medico_Crear(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico/medico_form.html'
    success_url = reverse_lazy('paciente:paciente_listar')