from django.db import models


class Paciente(models.Model):

    cedula = models.FloatField(null=True, blank=True, default=None)
    correo = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.name, self.cedula, self.correo, self.celular)
    
    