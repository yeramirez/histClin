from django.conf.urls import url, include
from apps.pacientes.views import index, paciente_view, paciente_list,paciente_edit,paciente_delete,paciente_mostrar
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    url(r'^nuevo$', login_required(paciente_view.as_view()), name='paciente_crear'),
    url(r'^mostrar$',login_required( paciente_mostrar.as_view()), name='paciente_mostrar'),
    url(r'^listar$', login_required(paciente_list.as_view()), name='paciente_listar'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(paciente_edit.as_view()), name='paciente_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(paciente_delete.as_view()), name='paciente_eliminar'),
]