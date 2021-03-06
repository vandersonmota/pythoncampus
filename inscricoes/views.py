# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.create_update import create_object
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from models import Palestra, Inscrito, MiniCurso
from forms import FormularioInscrito

minicursos_dia_27 = MiniCurso.objects.filter(data__day=27).order_by('horario')
minicursos_dia_28 = MiniCurso.objects.filter(data__day=28).order_by('horario')

def programacao(request):
    palestras_dia_27 = Palestra.objects.filter(data__day=27).order_by('horario')
    palestras_dia_28 = Palestra.objects.filter(data__day=28).order_by('horario')

    return render_to_response(
        'programacao.html',
        {
            'palestras_dia_27':palestras_dia_27,
            'palestras_dia_28':palestras_dia_28,
            'minicursos_dia_27':minicursos_dia_27,
            'minicursos_dia_28':minicursos_dia_28,
        },
        context_instance=RequestContext(request)
    )

def minicursos(request):
    return render_to_response(
        'minicursos.html',
        {
            'minicursos_dia_27':minicursos_dia_27,
            'minicursos_dia_28':minicursos_dia_28,
        },
        context_instance=RequestContext(request)
    )

