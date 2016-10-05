from django.conf.urls import url, include
from apps.historia.views import  historia_view, historia_edit,historia_list
from apps.pacientes.views import paciente_list
# At the top of your urls.py file, add the following line:
from django.conf import settings
from django.contrib.auth.decorators import login_required
# UNDERNEATH your urlpatterns definition, add the following two lines:

        
urlpatterns = [
   
    url(r'^nuevo$',login_required( historia_view.as_view()), name='historia_crear'),
    url(r'^list/(?P<pk>\d+)/$',login_required( historia_list.as_view()), name='historia_mostrar'),
     
    ]