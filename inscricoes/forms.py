from django import forms
from django.contrib.localflavor.br.forms import BRCPFField
from models import Inscrito, MiniCurso

class FormularioInscrito(forms.ModelForm):
    cpf = BRCPFField(label='CPF')
    minicurso = forms.ModelMultipleChoiceField(
        queryset=MiniCurso.objects.all(),
        widget = forms.widgets.CheckboxSelectMultiple,
        required = False)

    class Meta:
        model = Inscrito
        exclude = ('estado',)

    def padronizar_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        cpf = cpf.replace('.','').replace('-','').replace(' ','')
        self.cleaned_data['cpf'] = cpf
        
    def padronizar_campos(self):
        nome = self.cleaned_data.get('nome')
        self.cleaned_data['nome'] = nome.upper()
        
        instituicao = self.cleaned_data.get('instituicao')
        self.cleaned_data['instituicao'] = instituicao.upper()

    def save(self, force_insert=False, force_update=False, commit=True):
        self.padronizar_cpf()
        self.padronizar_campos()
        inscrito = super(FormularioInscrito, self).save(commit=True)
        minicursos = self.cleaned_data.get('minicurso',[])
        for minicurso in minicursos:
            inscrito.inscrever(minicurso)
        inscrito.save()
        return inscrito

