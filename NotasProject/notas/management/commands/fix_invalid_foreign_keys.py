# notas/management/commands/fix_invalid_foreign_keys.py

from django.core.management.base import BaseCommand
from notas.models import Nota
from asignaturas.models import Asignatura
from alumnos.models import Alumno

class Command(BaseCommand):
    help = 'Fix invalid foreign keys in notas_nota table'

    def handle(self, *args, **kwargs):
        notas = Nota.objects.all()
        invalid_notas_asignatura = 0
        fixed_notas_asignatura = 0
        invalid_notas_alumno = 0
        fixed_notas_alumno = 0

        for nota in notas:
            # Check asignatura_id
            if not Asignatura.objects.filter(id=nota.asignatura_id).exists():
                invalid_notas_asignatura += 1
                self.stdout.write(
                    self.style.ERROR(f'Nota ID {nota.id} has an invalid asignatura_id: {nota.asignatura_id}')
                )
                # Update the invalid asignatura_id to a valid one (e.g., the first one found)
                valid_asignatura_id = Asignatura.objects.first().id  # Ensure there's at least one Asignatura
                nota.asignatura_id = valid_asignatura_id
                nota.save()
                fixed_notas_asignatura += 1

            # Check alumno_id
            if not Alumno.objects.filter(id=nota.alumno_id).exists():
                invalid_notas_alumno += 1
                self.stdout.write(
                    self.style.ERROR(f'Nota ID {nota.id} has an invalid alumno_id: {nota.alumno_id}')
                )
                # Update the invalid alumno_id to a valid one (e.g., the first one found)
                valid_alumno_id = Alumno.objects.first().id  # Ensure there's at least one Alumno
                nota.alumno_id = valid_alumno_id
                nota.save()
                fixed_notas_alumno += 1

        self.stdout.write(
            self.style.SUCCESS(f'Found {invalid_notas_asignatura} invalid notas due to asignatura_id and fixed {fixed_notas_asignatura} of them.')
        )
        self.stdout.write(
            self.style.SUCCESS(f'Found {invalid_notas_alumno} invalid notas due to alumno_id and fixed {fixed_notas_alumno} of them.')
        )
