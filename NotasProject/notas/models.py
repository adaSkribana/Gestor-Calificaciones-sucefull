from django.db import models
from asignaturas.models import Asignatura 
from alumnos.models import Alumno



class Nota(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    puntaje = models.FloatField()

    def __str__(self):
        return f"{self.alumno} - {self.asignatura}: {self.puntaje}"
