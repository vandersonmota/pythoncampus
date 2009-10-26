from django.conf.urls.defaults import *
from django.conf import settings
from inscricoes.models import Palestra, Ministrante
from inscricoes.forms import FormularioInscrito

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

object_list = 'django.views.generic.list_detail.object_list'
object_detail = 'django.views.generic.list_detail.object_detail'

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$','views.index'),
    (r'^inscricao_principal/$','inscricoes.views.inscricao_base_view'),
    (r'^inscricao/$','django.views.generic.create_update.create_object',
        {'form_class': FormularioInscrito,'template_name': 'inscricao.html',
        'post_save_redirect': '/'}),
    (r'^programacao/', 'inscricoes.views.programacao'),
    (r'^ministrante/(?P<object_id>\d+)',object_detail,
     {'queryset': Ministrante.objects.all(),'template_name':'detalhes_ministrante.html',}
    ),
    (r'^media/(.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}),
)
