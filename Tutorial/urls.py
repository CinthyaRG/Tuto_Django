from django.conf.urls import url
from Tutorial.views import *

urlpatterns = [
    url(
        r'^$',
        Home.as_view(),
        name='home'),
    url(
        r'^registro$',
        Registro.as_view(),
        name='registro'),
    url(
        r'^resultado$',
        HomeExtra.as_view(),
        name='resultado'),
]