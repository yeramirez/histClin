from django.db import models
from apps.medico.models import Medico
from django.contrib import admin
    
 #Modelo de datos de la historia clinica   
# Create your models here.

class Paciente(models.Model):
        
        nombre = models.CharField(max_length = 20)
        apellidos = models.CharField(max_length = 20)
        mail = models.EmailField()
        Sex=(('M','Masculino'),('F','Femenino'),('O','Otro'))
        sexo = models.CharField(max_length= 1,choices=Sex)
        edad = models.IntegerField()
        Doc  = models.IntegerField(unique=True)
        domicilio = models.CharField(max_length=30)
        colegio = models.CharField(max_length=10)
        grado = models.IntegerField()
        Medico = models.ForeignKey(Medico, null=True, blank=True, on_delete=models.CASCADE)
        madre = models.CharField(max_length=10)
        padre = models.CharField(max_length=10)
        telefono = models.IntegerField()
        
        
        def __str__(self):
            return '{} {} {}'.format(self.nombre,self.apellidos,self.Doc)
   