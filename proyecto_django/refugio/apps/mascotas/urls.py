from django.conf.urls import url

from apps.mascotas.views import index

urlpatterns = [
    url(r'^index', index),
]