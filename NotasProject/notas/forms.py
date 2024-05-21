from django import forms
from .models import  Nota, Alumno, Asignatura
class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['alumno', 'asignatura', 'puntaje']
    alumno = forms.ModelChoiceField(queryset=Alumno.objects.all(), label='Alumno')
    asignatura = forms.ModelChoiceField(queryset=Asignatura.objects.all(), label='Asignatura')


