from django.db import models

# Create your models here.
class tareas(models.Model):
    nombre = models.CharField(max_length=32, null=True, blank=True)
    estado = models.CharField(max_length=32, null=True, blank=True)
    responsable = models.CharField(max_length=32, null=True, blank=True)
    fecha = models.CharField(max_length=32, null=True, blank=True)