from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import AlumnoForm
from .models import Alumno

@login_required
def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos/lista_alumnos.html', {'alumnos': alumnos})

@login_required
def detalle_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    return render(request, 'alumnos/detalle_alumno.html', {'alumno': alumno})

@login_required
def nuevo_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'alumnos/nuevo_alumno.html', {'form': form})

@login_required
def editar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'alumnos/editar_alumno.html', {'form': form, 'alumno': alumno})
