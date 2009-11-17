from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import FormularioContato
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage

def index(request):
    return render_to_response(
        'index.html',
        context_instance=RequestContext(request)
    )
    
def contato(request):
    if request.method  == 'POST':
        formulario_contato = FormularioContato(request.POST)
        if formulario_contato.is_valid():
          nome = request.POST.get('nome')
          email = request.POST.get('email')
          assunto = request.POST.get('assunto')
          mensagem = request.POST.get('mensagem')
          mail = EmailMessage(assunto,mensagem,email,['pythoncampus@iff.edu.br'])
          try:
            mail.send()
            return HttpResponseRedirect('/sucesso_contato/')
          except:
            return HttpResponse('Erro: Problemas tecnicos no servidor de email.')
        else:
            return render_to_response(
                'contato.html',
                {'form':formulario_contato},
                context_instance=RequestContext(request)
            )
    else:
        form = FormularioContato()
        return render_to_response(
            'contato.html',
            {'form':form},
            context_instance=RequestContext(request)
        )
