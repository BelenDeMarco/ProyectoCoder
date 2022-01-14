from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TorneoFormulario (forms.Form):
    
    nombre = forms.CharField(max_length=40)
    tipo= forms.CharField(max_length=40)
    categoria = forms.CharField(max_length=40)
    sede = forms.CharField(max_length=40)
    inicio = forms.DateField(input_formats= ["%d/%m/%Y"],help_text= "Ingrese dd/mm/aaaa")


class SedeFormulario (forms.Form):

    nombre = forms.CharField(max_length=40)
    ubicacion = forms.CharField(max_length=40)
    estacionamiento = forms.BooleanField (required=False)
    vestuarios = forms.BooleanField (required=False)


class UserRegisterForm(UserCreationForm):
  
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    username = forms.CharField(label='Usuario')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
      
    
    
   
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2'] 
        

class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña')
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)  
 
    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2']
