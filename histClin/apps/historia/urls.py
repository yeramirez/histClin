from django.conf.urls import url, include
from apps.historia.views import index, historia_view, historia_edit
from apps.pacientes.views import paciente_list
# At the top of your urls.py file, add the following line:
from django.conf import settings

# UNDERNEATH your urlpatterns definition, add the following two lines:

        
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', historia_view.as_view(), name='historia_crear'),
    url(r'^editar/(?P<pk>\d+)/$', historia_edit.as_view(), name='historia_editar'),
 ]