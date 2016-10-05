from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.historia.forms import HistoriaForm
from apps.historia.models import Historia
from apps.pacientes.models import Paciente
from django.views.generic import ListView,CreateView,UpdateView
from django.core.urlresolvers import reverse_lazy
#Instalar para campo de formulario con fecha
#https://github.com/nkunihiko/django-bootstrap3-datetimepicker



#----------Vista para  las historias 

class historia_view(CreateView):
    
    model = Historia
    form_class = HistoriaForm
    template_name = 'historia/historia_create.html'
    success_url = reverse_lazy('paciente:paciente_listar')    
    
class historia_edit(UpdateView):
    model = Historia
    form_class = HistoriaForm
    template_name = 'historia/historia_create.html'
    success_url = reverse_lazy('paciente:paciente_listar')
    

class historia_list(ListView):
    
    model = Historia
    template_name = 'historia/historia_mostrar.html'
    def get_queryset(self):
      
       return Historia.objects.get(pk=self.kwargs['pk'])
    
    
    def get_context_data(self,  **kwargs):
        context=super(historia_list,self).get_context_data(**kwargs)
        context['paciente']=Paciente.objects.filter(historia__id=self.kwargs['pk'])
        return context
    
    