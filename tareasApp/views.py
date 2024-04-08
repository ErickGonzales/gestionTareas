from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import tareas

lista_tareas = []
# Create your views here.
def index(request):
    tareasTotales = tareas.objects.all()
    return render(request, 'index.html', {
        'tareasTotales':tareasTotales
    })

def nuevaTarea(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion  = request.POST.get('descripcion')
        fecha = request.POST.get('fecha')
        responsable = request.POST.get('responsable')
        tareas.objects.create(
            nombre=nombre,
            estado='EN PROGRESO',
            responsable = responsable,
            fecha = fecha
        )
        lista_tareas.append([nombre, descripcion, fecha, 'EN PROGRESO', responsable])
        print(lista_tareas)
        return HttpResponseRedirect(reverse('tareasApp:index'))
    return render(request, 'nuevaTarea.html')