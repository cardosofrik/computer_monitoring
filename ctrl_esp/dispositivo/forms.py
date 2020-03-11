from django import  forms

class EnderecoForms(forms.Form):
    ip = forms.CharField(max_length=120)
    porta = forms.CharField(max_length=120)
    nome = forms.CharField(max_length=120)
