# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.create_update import create_object
from django.http import HttpResponseRedirect
from models import MiniEvento,Inscrito
from forms import FormularioInscrito

def inscricao_base_view(request):
    return render_to_response(
        'index.html',
        context_instance=RequestContext(request)
    )
    
def minicursos(request):
    minicursos_dia_27 = MiniEvento.objects.filter(
        tipo='minicurso',
        data__day=27).order_by('horario')
    minicursos_dia_28 = MiniEvento.objects.filter(
        tipo='minicurso',
        data__day=28).order_by('horario')
    
    return render_to_response(
        'minicursos.html',
        {
            'minicursos_dia_27':minicursos_dia_27,
            'minicursos_dia_28':minicursos_dia_28,
        },
        context_instance=RequestContext(request)
    )