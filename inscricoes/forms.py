from django import forms
from django.contrib.localflavor.br.forms import BRCPFField
from models import Inscrito, MiniCurso

class FormularioInscrito(forms.ModelForm):
    cpf = BRCPFField(label='CPF')
    minicurso = forms.ModelMultipleChoiceField(
        queryset=MiniCurso.objects.all(),
        widget = forms.widgets.CheckboxSelectMultiple)
    
    class Meta:
        model = Inscrito
        exclude = ('estado',)
        
    def save(self, force_insert=False, force_update=False, commit=True):
        inscrito = super(FormularioInscrito, self).save(commit=True)
        minicursos = self.cleaned_data.get('minicurso',[])
        for minicurso in minicursos: 
            inscrito.inscrever(minicurso)
        inscrito.save()


