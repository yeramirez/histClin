from django.contrib import admin

from apps.pacientes.models import  Paciente



   
      
#class DatosPersonales(admin.ModelAdmin):
 #   fieldsets = [
  #      ('Datos de Contacto', {'fields': [('nombre',
   #                                       'apellidos','edad','sexo', 'Doc'),
   #                                       ('domicilio','colegio','grado')] }),
    #             
     #   ('Informacion Acudiente', {'fields': ['madre','padre','telefono'] }),
      #  ('Medico de familia', {'fields': ['Medico'], 'classes': ['collapse']}),
       # ('Observaciones y Antecedentes', {'fields': ['observacion_Entorno_familiar',
        #                                             'motivo_consulta','antecedentes_personales','alergicos',
         #                                            'vacuna'],
          #                                 'classes': ['collapse']}),
        
       # ('Examenes y observaciones', {'fields': ['examen_fisico',
        #                                             'fc','fr','pc','talla','peso','pa','imc','av','cabeza_cuello',
         #                                            'cardio_pulmonar','abdomen','extremidades','piel_anexos',
          #                                           'observaciones','fecha_creacion'],
           #                                'classes': ['collapse']}),
    #]
   
    #list_display = ('nombre','apellidos','Doc','telefono')
    #search_fields = ('nombre', 'Doc')
    

       

admin.site.register(Paciente)
