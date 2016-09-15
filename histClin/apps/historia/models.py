from django.db import models
from apps.pacientes.models import Paciente


# Create your models here.
class Historia(models.Model):
        pacientes=models.ForeignKey(Paciente,blank=False, on_delete=models.CASCADE)        
        observacion_Entorno_familiar = models.TextField()
        motivo_consulta =  models.TextField()
        antecedentes_personales = models.TextField()
        alergicos = models.CharField(max_length=100)
        vacuna = models.ImageField(upload_to='vacuna')
        examen_fisico= models.TextField()
        fc = models.IntegerField()
        fr = models.IntegerField()                
        pc = models.IntegerField()
        talla = models.FloatField()
        peso = models.IntegerField()
        pa = models.IntegerField()
        #este campo se le debe asignar peso dividido altura elevado a la 2 
        imc = models.FloatField()
        av = models.IntegerField()
        cabeza_cuello = models.CharField(max_length=100)
        cardio_pulmonar = models.CharField(max_length=100)
        abdomen = models.CharField(max_length=100)
        extremidades = models.CharField(max_length=100)
        piel_anexos = models.CharField(max_length=100)
        observaciones = models.TextField()
        fecha_creacion = models.DateField()
        
        
        def __str__(self):
            return '{}'.format(self.fecha_creacion)
   
        