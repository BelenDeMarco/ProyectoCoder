from django import forms

class TorneoFormulario (forms.Form):
    
    nombre = forms.CharField(max_length=40)
    tipo= forms.CharField(max_length=40)
    categoria = forms.CharField(max_length=40)
    sede = forms.CharField(max_length=40)
    inicio = forms.DateField(input_formats= ["%d/%m/%Y"],help_text= "Ingrese dd/mm/aaaa")