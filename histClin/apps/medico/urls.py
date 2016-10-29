from django.conf.urls import url, include
from apps.medico.views import Medico_Crear,Medico_list,Medico_edit,Medico_delete
from django.contrib.auth.decorators import login_required
urlpatterns = [
    
    url(r'^registrar$', login_required(Medico_Crear.as_view()), name='medico_crear'),
    url(r'^listar$', Medico_list.as_view(), name='medico_listar'),
    url(r'^editar/(?P<pk>\d+)/$', Medico_edit.as_view(), name='medico_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', Medico_delete.as_view(), name='medico_eliminar'),
   
]
