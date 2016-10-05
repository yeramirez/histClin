from django import forms
from apps.medico.models import Medico
from django.contrib.auth.forms import UserCreationForm
from bootstrap3_datetime.widgets import DateTimePicker

TITLE_SEXO = (
    ('M', 'M'),
    ('F', 'F'),
    
)

class MedicoForm(UserCreationForm):
    
    class Meta:
        model = Medico
        
        fields =[
            'username',  
            'first_name', 
            'last_name',
            'email',
            'sexo',
            'especialidad',
            'telefono',
            'password1',
            'password2',
            'especialidad',
            'telefono',
            'firma',
            'imgperfil',
         ]
        
        widgets = {
        
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'especialidad':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'password1':forms.TextInput(attrs={'class':'form-control','type':'password'}),
            'password2':forms.TextInput(attrs={'class':'form-control','type':'password'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}), 
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.Select(attrs={'class':'form-form-control'},choices=TITLE_SEXO),
            'email':forms.EmailInput(attrs={'class':'form-form-control'}),
            'especialidad':forms.TextInput(attrs={'class':'form-control'}), 
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'firma':forms.FileInput(attrs={'class':'fileupload-new'}),
            'imgperfil':forms.FileInput(attrs={'class':'fileupload-new'}),
        
        }