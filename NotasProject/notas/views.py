from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import NotaForm
from .models import Nota

@login_required
def lista_notas(request):
    notas = Nota.objects.all()
    return render(request, 'notas/lista_notas.html', {'notas': notas})

@login_required
def nueva_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaForm()
    return render(request, 'notas/crear_nota.html', {'form': form})

@login_required
def editar_nota(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaForm(instance=nota)
    return render(request, 'notas/crear_nota.html', {'form': form})
