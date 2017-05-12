from Tutorial.models import *
from rest_framework import viewsets
from Tutorial_API.serializers import UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Usuarios.objects.all().order_by('id')
    serializer_class = UsuarioSerializer

#class UsuarioViewSet(viewsets.ModelViewSet):
#    """
#   API endpoint that allows users to be viewed or edited.
#    """
#    queryset = Usuarios.objects.all().order_by('id')
#    serializer_class = UsuarioSerializer