from django.shortcuts import render
from django.views.generic import *


class Home (TemplateView):
    template_name = 'home.html'


class HomeExtra (TemplateView):
    template_name = 'home2.html'
