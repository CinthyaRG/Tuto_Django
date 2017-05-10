from django.shortcuts import render
from django.views.generic import CreateView

class Home(CreateView):
    template_name = 'Tutorial_Django/templates/Home.html'

    def get_context_data(self, **kwargs):
        context = super(
            PerfilMedico, self).get_context_data(**kwargs)
        user = self.request.user


usuario = Usuario.objects.get(user=user)

