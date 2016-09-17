from django import forms
from apps.pacientes.models import Paciente


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
            'Doc_id',
            'domicilio',
            'colegio',
            'grado',
            'Medico',
            'madre',
            'padre',
            'telefono',
            
            
           
        ]
        widgets = {
            
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.Select(attrs={'class':'form-form-control'},choices=TITLE_SEXO),
            'edad': forms.TextInput(attrs={'rows':'2','class':'form-control'}),
            'Doc_id': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.TextInput(attrs={'class':'form-control'}),
            'colegio': forms.TextInput(attrs={'class':'form-control'}),
            'grado': forms.TextInput(attrs={'class':'form-control'}),
            'Medico': forms.Select(attrs={'class':'form-control'}),
            'madre': forms.TextInput(attrs={'class':'form-control'}),
            'padre': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            
        }
        
        
                       