from django.conf.urls.defaults import *
from django.conf import settings
from inscricoes.models import Palestra, Ministrante, MiniCurso
from inscricoes.forms import FormularioInscrito

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

object_detail = 'django.views.generic.list_detail.object_detail'
create_object = 'django.views.generic.create_update.create_object'

propriedades_inscricao = {
    'form_class': FormularioInscrito,
    'template_name': 'inscricao.html',
    'post_save_redirect': '/sucesso_inscricao/',
    }

propriedades_ministrante = {
    'queryset': Ministrante.objects.all(),
    'template_name':'detalhes_ministrante.html',
    }

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$','views.index'),
    (r'^programacao/$', 'pythoncampus.inscricoes.views.programacao'),
    (r'^inscricao/$', create_object, propriedades_inscricao),
    #(r'^minicursos/', 'inscricoes.views.minicursos'),
    (r'^equipe/$',
        'django.views.generic.simple.direct_to_template',
        {'template':'equipe.html'}),
    (r'^equipe_site/$',
        'django.views.generic.simple.direct_to_template',
        {'template':'equipe_site.html'}),
    (r'^sucesso_inscricao/$',
        'django.views.generic.simple.direct_to_template',
        {'template':'sucesso_inscricao.html'}),
    (r'^local/$','django.views.generic.simple.direct_to_template',
        {'template':'local.html'}),
    (r'^ministrante/(?P<object_id>\d+)$', object_detail, propriedades_ministrante),
    (r'^contato/$', 'pythoncampus.views.contato'),
    (r'^sucesso_contato/$','django.views.generic.simple.direct_to_template',
        {'template':'sucesso_contato.html'}),
    (r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}
    ),
)

