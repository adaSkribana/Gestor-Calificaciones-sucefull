from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    contacto = models.CharField(max_length=100, null=True, blank=True)
    asignatura = models.ForeignKey('asignaturas.Asignatura', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre
