from django.db import models
from apps.medico.models import Medico
from apps.pacientes.models import Paciente

class Formulas(models.Model):
    medicos=models.ForeignKey(Medico, null=True, blank=True, on_delete=models.CASCADE)
    pacientes_f=models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)
    medicamento = models.CharField(max_length=30)
    dosificacion= models.CharField(max_length=30)
    cantidad = models.CharField(null=True,blank=True,max_length=30)
    medicamento2 = models.CharField(null=True,blank=True,max_length=30)
    dosificacion2= models.CharField(null=True,blank=True,max_length=30)
    cantidad2 = models.CharField(null=True,blank=True,max_length=30)
    medicamento3 = models.CharField(null=True,blank=True,max_length=30)
    dosificacion3= models.CharField(null=True,blank=True,max_length=30)
    cantidad3 = models.CharField(null=True,blank=True,max_length=30)
    observaciones=models.TextField(null=True,blank=True, max_length=30)
    recomendaciones=models.TextField(null=True, blank=True)
    fecha_creacion = models.DateField()
    hora=models.TimeField()
    def __str__(self):
            return '{}'.format(self.fecha_creacion)

# Create your models here.
