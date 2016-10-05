from django.db import models
from apps.medico.models import Medico
from apps.pacientes.models import Paciente

class Formulas(models.Model):
    medicos=models.ForeignKey(Medico, null=True, blank=True, on_delete=models.CASCADE)
    pacientes_f=models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)
    formula=models.TextField(null=True,blank=True)
    recomendaciones=models.TextField(null=True, blank=True)
    

# Create your models here.
