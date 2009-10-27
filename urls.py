from django.conf.urls.defaults import *
from django.conf import settings
from inscricoes.models import Palestra, Ministrante, MiniCurso
from inscricoes.forms import FormularioInscrito

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

object_detail = 'django.views.generic.list_detail.object_detail'

propriedades_ministrante = {
    'queryset': Ministrante.objects.all(),
    'template_name':'detalhes_ministrante.html',
    }

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$','views.index'),
    (r'^inscricao/','inscricoes.views.inscricao'),
    (r'^programacao/', 'inscricoes.views.programacao'),
    #(r'^minicursos/', 'inscricoes.views.minicursos'),
    (r'^equipe','django.views.generic.simple.direct_to_template',{'template':'equipe.html'}),
    (r'^ministrante/(?P<object_id>\d+)', object_detail, propriedades_ministrante),
    (r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}
    ),
)