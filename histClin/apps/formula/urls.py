from django.conf.urls import url, include
from apps.formula.views import  Formula_Crear,Formula_Listar,Recomendaciones_crear

# At the top of your urls.py file, add the following line:
from django.conf import settings
from django.contrib.auth.decorators import login_required
# UNDERNEATH your urlpatterns definition, add the following two lines:

        
urlpatterns = [
   
    url(r'^formula$', login_required(Formula_Crear.as_view()), name='formula_crear'),
    url(r'^list$',login_required( Formula_Listar.as_view()), name='formula_mostrar'),
    url(r'^recomendacion$', login_required(Recomendaciones_crear.as_view()), name='recomendacion_crear'),
    ]