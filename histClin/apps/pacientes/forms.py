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
        
        labels = {
            'nombre':'Nombre',
            'apellidos':'Apellidos',
            'sexo':'Sexo',
            'edad':'Edad',
            'Doc':'Documento',
            'domicilio':'Recidencia',
            'colegio':'Colegio',
            'grado':'Grado',
            'Medico':'Medico',
            'fecha_creacion':'Fecha De Creacion',
            'madre':'Madre',
            'padre':'Padre',
            'telefono':'Telefono',
            'observacion_Entorno_familiar':'Observacion Entorno Familiar',
            'motivo_consulta':'Motivo de Consulta',
            'antecedentes_personales':'Antecedentes Personales',
            'alergicos':'Alergicos',
            'vacuna':'Vacuna',
            'examen_fisico':'Examen Fisica',
            'fc':'Fc',
            'fr':'Fr',
            'pc':'Pc',
            'talla':'Talla',
            'peso':'Peso',
            'pa':'Pa',
            'imc':'Imc',
            'av':'Av',
            'cabeza_cuello':'Cabeza Cuello',
            'cardio_pulmonar':'Cardio Pulmonar',
            'abdomen':'Abdomen',
            'extremidades':'Extremidades',
            'piel_anexos':'Piel Anexos',
            'observaciones':'Observaciones',
        }
        widgets = {
            
            'nombre':forms.TextInput(attrs={'class':'form-group'}),
            'apellidos': forms.TextInput(attrs={'class':'form-group'}),
            'sexo': forms.Select(attrs={'class':'form-group'},choices=TITLE_SEXO),
            'edad': forms.TextInput(attrs={'class':'form-group'}),
            'Doc': forms.TextInput(attrs={'class':'form-group'}),
            'domicilio': forms.TextInput(attrs={'class':'form-group'}),
            'colegio': forms.TextInput(attrs={'class':'form-group'}),
            'grado': forms.TextInput(attrs={'class':'form-group'}),
            'Medico': forms.Select(attrs={'class':'form-group'}),
            'fecha_creacion' : DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False},attrs={'class':'form-group'}),
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
            'fc': forms.TextInput(attrs={'class':'form-control'}),
            'fr': forms.TextInput(attrs={'class':'form-control'}),
            'pc': forms.TextInput(attrs={'class':'form-control'}),
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