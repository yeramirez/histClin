from django.conf.urls import url, include
from apps.medico.views import index

urlpatterns = [
    url(r'^$', index),
]
