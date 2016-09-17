from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.historia.forms import HistoriaForm
from apps.historia.models import Historia
from django.views.generic import ListView,CreateView
from django.core.urlresolvers import reverse_lazy
#Instalar para campo de formulario con fecha
#https://github.com/nkunihiko/django-bootstrap3-datetimepicker

def index(request):
    return render(request, 'historia/index.html')

#----------Vista para  las historias 

class historia_view(CreateView):
    
    model = Historia
    form_class = HistoriaForm
    template_name = 'historia/historia_create.html'
    success_url = reverse_lazy('historia:paciente_listar')       

class historia_list(ListView):
    
    model = Historia
    form_class = HistoriaForm
    template_name = 'historia/historia_listar.html'
    success_url = reverse_lazy('historia:historia_create')
    