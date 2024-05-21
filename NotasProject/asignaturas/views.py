from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import AsignaturaForm
from .models import Asignatura

@login_required
def lista_asignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'asignaturas/lista_asignaturas.html', {'asignaturas': asignaturas})

@login_required
def detalle_asignatura(request, pk):
    asignatura = get_object_or_404(Asignatura, pk=pk)
    return render(request, 'asignaturas/detalle_asignatura.html', {'asignatura': asignatura})

@login_required
def nueva_asignatura(request):
    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_asignaturas')
    else:
        form = AsignaturaForm()
    return render(request, 'asignaturas/crear_asignatura.html', {'form': form})

@login_required
def editar_asignatura(request, pk):
    asignatura = get_object_or_404(Asignatura, pk=pk)
    if request.method == 'POST':
        form = AsignaturaForm(request.POST, instance=asignatura)
        if form.is_valid():
            form.save()
            return redirect('lista_asignaturas')
    else:
        form = AsignaturaForm(instance=asignatura)
        return render(request, 'asignaturas/crear_asignatura.html', {'form': form})

