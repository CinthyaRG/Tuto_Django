from django.conf.urls import url
from Tutorial.views import *

urlpatterns = [
    url(
        r'^$',
        Home.as_view(),
        name='home'),
    url(
        r'^Home2$',
        HomeExtra.as_view(),
        name='home2'),
]