from django.db import models

class Usuario(models.Model):

    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    correo = models.CharField(max_length=20)

    def get_name(self):
        return self.first_name + " " + self.last_name