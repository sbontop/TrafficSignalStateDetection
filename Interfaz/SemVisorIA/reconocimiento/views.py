from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SubirImagenForm
from .models import Imagen
from .IA import getResults

# Create your views here.
def cargar_imagen(request):
    form = SubirImagenForm()
    if request.method == 'POST':
        form = SubirImagenForm(request.POST, request.FILES)  
        if form.is_valid():
            imagen_guardada = form.save()
            return HttpResponseRedirect(reverse('mostrar_imagen', args = [imagen_guardada.id]))
    return render(request, 'cargar_imagen.html', locals())

def mostrar_imagen(request, id):
    try:
        imagen = Imagen.objects.get(pk=id)
    except:
        imagen = None 
    return render(request, 'mostrar_imagen.html', getResults(imagen))
