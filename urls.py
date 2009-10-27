from django.conf.urls.defaults import *
from django.conf import settings
from inscricoes.models import Palestra, Ministrante, MiniCurso
from inscricoes.forms import FormularioInscrito

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

object_list = 'django.views.generic.list_detail.object_list'
object_detail = 'django.views.generic.list_detail.object_detail'
create_object = 'django.views.generic.create_update.create_object'

propriedades_inscricao = {
    'form_class': FormularioInscrito,
    'template_name': 'inscricao.html',
    'post_save_redirect': '/'
    }

propriedades_ministrante = {
    'queryset': Ministrante.objects.all(),
    'template_name':'detalhes_ministrante.html',
    }

propriedades_minicursos = {
    'queryset': MiniCurso.objects.all().order_by('data').order_by('horario'),
    'template_name': 'minicursos.html',
    }

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$','views.index'),
    (r'^inscricao_principal/$', 'inscricoes.views.inscricao_base_view'),
    (r'^inscricao/$', create_object, propriedades_inscricao),
    (r'^programacao/', 'inscricoes.views.programacao'),
    (r'^minicursos/', object_list, propriedades_minicursos),
    (r'^ministrante/(?P<object_id>\d+)', object_detail, propriedades_ministrante),
    (r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}
    ),
)
