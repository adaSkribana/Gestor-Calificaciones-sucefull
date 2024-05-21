from django.shortcuts import render  # Mantén esta línea
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request, 'home.html')
