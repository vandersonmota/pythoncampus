from django import forms
from django.contrib.localflavor.br.forms import BRCPFField
from models import Inscrito,MiniEvento

class FormularioInscrito(forms.ModelForm):
    cpf = BRCPFField(label='CPF')
    minicurso = forms.ModelMultipleChoiceField(
        queryset=MiniEvento.objects.filter(tipo='minicurso'),
        widget = forms.widgets.CheckboxSelectMultiple)
    
    class Meta:
        model = Inscrito


