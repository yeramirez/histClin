from django import forms
from apps.pacientes.models import Paciente
from bootstrap3_datetime.widgets import DateTimePicker

TITLE_SEXO = (
    ('M', 'M'),
    ('F', 'F'),
    
)



class PacienteForm(forms.ModelForm):
    

    class Meta:
        model = Paciente
        
        fields = [
        
            'nombre',
            'apellidos',
            'sexo',
            'edad',
            'Doc',
            'domicilio',
            'colegio',
            'grado',
            'Medico',
            'fecha_creacion',
            'madre',
            'padre',
            'telefono',
            'telefono',
            'observacion_Entorno_familiar',
            'motivo_consulta',
            'antecedentes_personales',
            'alergicos',
            'vacuna',
            'examen_fisico',
            'fc',
            'fr',
            'pc',
            'talla',
            'peso',
            'pa',
            'imc',
            'av',
            'cabeza_cuello',
            'cardio_pulmonar',
            'abdomen',
            'extremidades',
            'piel_anexos',
            'observaciones',
            
        ]
        widgets = {
            
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.Select(attrs={'class':'form-form-control'},choices=TITLE_SEXO),
            'edad': forms.TextInput(attrs={'rows':'2','class':'form-control'}),
            'Doc': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.TextInput(attrs={'class':'form-control'}),
            'colegio': forms.TextInput(attrs={'class':'form-control'}),
            'grado': forms.TextInput(attrs={'class':'form-control'}),
            'Medico': forms.Select(attrs={'class':'form-control'}),
            'fecha_creacion' : DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False},attrs={'class':'form-control'}),
            
            'madre': forms.TextInput(attrs={'class':'form-control'}),
            'padre': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            
            'observacion_Entorno_familiar': forms.Textarea(attrs={'class':'form-control'}),
            'antecedentes_personales': forms.TextInput(attrs={'class':'form-control'}),
            'motivo_consulta': forms.Textarea(attrs={'class':'form-control'}),
            'antecedentes_personales': forms.Textarea(attrs={'class':'form-control'}),
            'alergicos': forms.TextInput(attrs={'class':'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
            'examen_fisico': forms.TextInput(attrs={'class':'form-control'}),
            'fc': forms.TextInput(attrs={'class':'form-control','size':'2'}),
            'fr': forms.TextInput(attrs={'class':'form-control','size':'2'}),
            'pc': forms.TextInput(attrs={'class':'form-control','size':'2'}),
            'talla': forms.TextInput(attrs={'class':'form-control'}),
            'peso': forms.TextInput(attrs={'class':'form-control'}),
            'pa': forms.TextInput(attrs={'class':'form-control'}),
            'imc': forms.TextInput(attrs={'class':'form-control'}),
            'av': forms.TextInput(attrs={'class':'form-control'}),
            'cabeza_cuello': forms.TextInput(attrs={'class':'form-control'}),
            'cardio_pulmonar': forms.TextInput(attrs={'class':'form-control'}),
            'abdomen': forms.TextInput(attrs={'class':'form-control'}),
            'extremidades': forms.TextInput(attrs={'class':'form-control'}),
            'piel_anexos': forms.TextInput(attrs={'class':'form-control'}),
            'observaciones': forms.Textarea(attrs={'class':'form-control'}),
            
          
        }
        
        
                       