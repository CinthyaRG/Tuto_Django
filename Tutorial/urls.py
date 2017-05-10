from django.conf.urls import url
from Tutorial.views import *

urlpatterns = [
    url(
        r'^home/',
        Home.as_view(),
        name='home'
    ),

]