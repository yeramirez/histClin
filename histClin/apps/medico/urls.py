from django.conf.urls import url, include
from apps.medico.views import Medico_Crear
from django.contrib.auth.decorators import login_required
urlpatterns = [
    
    url(r'^registrar$', login_required(Medico_Crear.as_view()), name='medico_crear'),
   
]
