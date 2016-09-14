from django.conf.urls import url, include
from apps.historia.views import index, historia_view, historia_list
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', historia_view.as_view(), name='historia_crear'),
    url(r'^listar$', historia_list.as_view(), name='historia_listar'),
    
]