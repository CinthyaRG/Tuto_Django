from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import *
from Tutorial.forms import UsuariosForm
from Tutorial.models import Usuarios


class Home (TemplateView):
    template_name = 'base.html'


class Registro (FormView):
    template_name = 'registro.html'
    form_class = UsuariosForm

    def get_context_data(self, **kwargs):
        context = super(
            Registro, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        post_values = request.POST.copy()
        form = UsuariosForm(post_values)
        if form.is_valid():
            # Guardamos los datos
            user= form.save()
            user.first_name = post_values['first_name']
            user.last_name = post_values['last_name']
            user.email = post_values['email']
            user.save()

            return HttpResponseRedirect(reverse_lazy('exitoso'))
        else:
            return render(request,'registro.html',{'form': form})


class HomeExtra (TemplateView):
    template_name = 'resultado.html'


class Exitoso (TemplateView):
    template_name = 'exitoso.html'

class VerUsuarios(TemplateView):
    template_name = 'ver_usuarios.html'

    def get_context_data(self, **kwargs):
        context = super(
            VerUsuarios, self).get_context_data(**kwargs)
        usuarios = Usuarios.objects.all()
        context['usuarios'] = usuarios
        return context

