from django.conf.urls import url, include
from apps.pacientes.views import index, paciente_view, paciente_list,paciente_edit,paciente_delete
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', paciente_view.as_view(), name='paciente_crear'),
    url(r'^listar$', paciente_list.as_view(), name='paciente_listar'),
    url(r'^editar/(?P<pk>\d+)/$', paciente_edit.as_view(), name='paciente_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', paciente_delete.as_view(), name='paciente_eliminar'),
]