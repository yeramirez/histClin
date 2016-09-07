from django.db import models

# Create your models here.

class Medico(models.Model):
       nombre = models.CharField(max_length=50)
       apellidos = models.CharField(max_length=20)
       especialidad = models.CharField(max_length=50)
       telefono = models.CharField(max_length=12)
       firma = models.ImageField(upload_to='firma')
       
                
        
        
       def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)