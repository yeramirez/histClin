from django.db import models
from apps.medico.models import Medico
from django.contrib import admin

class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)


# Create your models here.
class Paciente(models.Model):
        nombre = models.CharField(max_length = 20)
        apellidos = models.CharField(max_length = 20)
        Sex=(('M','Masculino'),('F','Femenino'),('O','Otro'))
        sexo = models.CharField(max_length= 1,choices=Sex)
        edad = models.IntegerField()
        Doc  = models.IntegerField()
        domicilio = models.CharField(max_length=30)
        colegio = models.CharField(max_length=10)
        grado = models.IntegerField()
        Medico = models.ForeignKey(Medico, null=True, blank=True, on_delete=models.CASCADE)
        fecha_creacion = models.DateField()
        madre = models.CharField(max_length=10)
        padre = models.CharField(max_length=10)
        telefono = models.IntegerField()
        observacion_Entorno_familiar = models.CharField(max_length=4000)
        motivo_consulta = models.CharField(max_length=4000)
        antecedentes_personales = models.CharField(max_length=100)
        alergicos = models.CharField(max_length=100)
        vacuna = models.ManyToManyField(Vacuna, blank=True)
        examen_fisico= models.CharField(max_length=100)
        fc = models.IntegerField()
        fr = models.IntegerField()                
        pc = models.IntegerField()
        talla = models.IntegerField()
        peso = models.IntegerField()
        pa = models.IntegerField()
        #este campo se le debe asignar peso dividido altura elevado a la 2 
        imc = models.IntegerField()
        av = models.IntegerField()
        cabeza_cuello = models.CharField(max_length=100)
        cardio_pulmonar = models.CharField(max_length=100)
        abdomen = models.CharField(max_length=100)
        extremidades = models.CharField(max_length=100)
        piel_anexos = models.CharField(max_length=100)
        observaciones = models.TextField()
        
        def __str__(self):
            return '{} '.format(self.nombre)

