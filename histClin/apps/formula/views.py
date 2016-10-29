from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.formula.forms import FormulaForm
from apps.formula.models import Formulas
from apps.pacientes.models import Paciente
from apps.medico.models import Medico

from django.views.generic import ListView,CreateView,UpdateView
from django.core.urlresolvers import reverse_lazy
#Instalar para campo de formulario con fecha
#https://github.com/nkunihiko/django-bootstrap3-datetimepicker



#----------Vista para  las formulas

class Formula_Crear(CreateView):
    
    model = Formulas
    form_class = FormulaForm
    template_name = 'formula/formula.html'
    
    
    def post(self, request,  *args, **kwargs ):
        if request.method == 'POST':
                form = FormulaForm(request.POST)
                if form.is_valid():
                        form.save()
                        buscar = request.POST['fecha_creacion']
                        hora = request.POST['hora']
                        paciente=request.POST['pacientes_f']
                        medicos=request.POST['medicos']
                        pacientes=Paciente.objects.filter(pk=paciente)
                        medicosl=Medico.objects.filter(pk=medicos)
                        print(medicosl)
                        formu =  Formulas.objects.filter(fecha_creacion=buscar,hora=hora)
      
                        return render(request,'formula/formula_list.html', {'formu':formu, 'pacientes':pacientes,'medicos':medicosl })
        else:
            form = MascotaForm()
        return render(request, self.template_name, {'form':form})            
    
class Formula_Listar(ListView):
        
    model = Formulas
   
  