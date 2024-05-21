from django.db import models

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.nombre} Descripccion: {self.descripcion}"
