# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.create_update import create_object
from models import MiniEvento,Inscrito
from forms import FormularioInscrito

def inscricao_base_view(request):
    return render_to_response(
        'index.html',
        context_instance=RequestContext(request)
    )
    
def inscricao(request):
    if request.method == 'post':
        pass
    else:
        return create_object(request,
                             form_class = FormularioInscrito,
                             template_name = 'inscricao.html',
                             post_save_redirect = '/')