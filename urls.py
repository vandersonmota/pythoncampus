from django.conf.urls.defaults import *
from inscricoes.models import MiniEvento
from inscricoes.forms import FormularioInscrito

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


object_list = 'django.views.generic.list_detail.object_list'
urlpatterns = patterns('',
    # Example:
    # (r'^pythoncampus/', include('pythoncampus.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$','views.index'),
    (r'^inscricao_principal/$','inscricoes.views.inscricao_base_view'),
    (r'^inscricao/$','django.views.generic.create_update.create_object',
     {'form_class': FormularioInscrito,'template_name': 'inscricao.html',
        'post_save_redirect': '/'}),
    (r'^palestras/$', object_list,
     {'queryset':MiniEvento.objects.filter(tipo='palestra'), 'template_name':'palestras.html'}),
    (r'^minicursos/', object_list,
     {'queryset':MiniEvento.objects.filter(tipo='minicurso'), 'template_name':'minicursos.html'})
)
