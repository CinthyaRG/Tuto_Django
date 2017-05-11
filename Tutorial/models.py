from django.db import models


class Usuarios(models.Model):

    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=30)

    def get_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return str(self.id) + " " + self.first_name + " " + self.last_name