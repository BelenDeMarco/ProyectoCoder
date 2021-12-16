from django import forms

class JugadorFormulario (forms.Form):

    nombre = forms.CharField(max_length= 40)
    apellido = forms.CharField (max_length= 40 )
    habilitado = forms.BooleanField (required= False)