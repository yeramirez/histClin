from django import forms
from apps.formula.models import Formulas
from bootstrap3_datetime.widgets import DateTimePicker

TITLE_SEXO = (
    ('M', 'M'),
    ('F', 'F'),
    
)

class FormulaForm(forms.ModelForm):
    
    class Meta:
        model = Formulas
        
        fields =[
            'fecha_creacion',
            'hora',
            'medicos',  
            'pacientes_f', 
            'observaciones',
            'recomendaciones',
            'medicamento',
            'dosificacion',
            'cantidad',
            'medicamento2',
            'dosificacion2',
            'cantidad2',
            'medicamento3',
            'dosificacion3',
            'cantidad3',
            
        
         ]
        
        widgets = {
               
            'medicos': forms.Select(attrs={'class':'form-form-control'}),
            'pacientes_f': forms.Select(attrs={'class':'form-form-control'}),
            'observaciones': forms.Textarea(attrs={'class':'form-control'}),
            'recomendaciones':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_creacion' : forms.TextInput(attrs={'class':'form-control date-picker','data-date-format':'yyyy-mm-dd'}),
            'hora' : forms.TextInput( attrs={"data-date-format": "hh:mm:ss A",'class':'form-control'}),
            'medicamento': forms.TextInput(attrs={'class':'form-control'}),
            'dosificacion': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad': forms.TextInput(attrs={'class':'form-control'}),
            'medicamento2': forms.TextInput(attrs={'class':'form-control'}),
            'dosificacion2': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad2': forms.TextInput(attrs={'class':'form-control'}),
            'medicamento3': forms.TextInput(attrs={'class':'form-control'}),
            'dosificacion3': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad3': forms.TextInput(attrs={'class':'form-control'}),
            
            
        }