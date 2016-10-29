from django import forms
from apps.historia.models import Historia
from bootstrap3_datetime.widgets import DateTimePicker

TITLE_SEXO = (
    ('M', 'M'),
    ('F', 'F'),
    
)

class HistoriaForm(forms.ModelForm):
    
    class Meta:
        model = Historia
        
        fields =[
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
            'fecha_creacion',
            'pacientes',
                   
        ]
        
        widgets = {
        
            'pacientes':forms.Select(attrs={'class':'form-control search-select'}),
            'observacion_Entorno_familiar': forms.Textarea(attrs={'class':'form-control'}),
            'antecedentes_personales': forms.TextInput(attrs={'class':'form-control'}),
            'motivo_consulta': forms.Textarea(attrs={'class':'form-control'}),
            'antecedentes_personales': forms.Textarea(attrs={'class':'form-control'}),
            'alergicos': forms.TextInput(attrs={'class':'form-control'}),
            'vacuna': forms.FileInput(attrs={'class':'fileupload-new'}),
            'examen_fisico': forms.Textarea(attrs={'class':'form-control'}),
            'fc': forms.TextInput(attrs={'class':'form-control','size':'2'}),
            'fr': forms.TextInput(attrs={'class':'form-control','size':'2'}),
            'pc': forms.TextInput(attrs={'class':'form-control','size':'2'}),
            'talla': forms.TextInput(attrs={'class':'form-control','onkeyUp':"Imc()"}),
            'peso': forms.TextInput(attrs={'class':'form-control','onkeyUp':"Imc()"}),
            'pa': forms.TextInput(attrs={'class':'form-control'}),
            'imc': forms.TextInput(attrs={'class':'form-control','readonly':"Imc()"}),
            'av': forms.TextInput(attrs={'class':'form-control'}),
            'cabeza_cuello': forms.TextInput(attrs={'class':'form-control'}),
            'cardio_pulmonar': forms.TextInput(attrs={'class':'form-control'}),
            'abdomen': forms.TextInput(attrs={'class':'form-control'}),
            'extremidades': forms.TextInput(attrs={'class':'form-control'}),
            'piel_anexos': forms.TextInput(attrs={'class':'form-control'}),
            'observaciones': forms.Textarea(attrs={'class':'form-control'}),
            'fecha_creacion' : forms.TextInput(attrs={'class':'form-control date-picker', 'data-date-format':'yyyy-mm-dd'}),
            
        }