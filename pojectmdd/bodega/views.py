from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import BodegueroForm, BodegaForm, ElementoForm, TieneForm
from .models import Bodeguero, Elemento, Bodega, Delegacion, Tiene
# from .forms import BodegaForm, DelegacionForm, UniversidadForm, BodegueroForm, ElementoForm, CiudadForm, RegionForm, DeportistaForm, TieneForm

# Create your views here.


def bodeguero(request):
    bodeguero = Bodeguero.objects.all()
    return render(request, 'bodeguero.html', {'bodeguero': bodeguero})


def main(request):
    return render(request, 'index.html', {})


def home(request):
    return render(request, 'home.html', {})


def elementos(request):
    elementos = Elemento.objects.all()
    return render(request, 'elementos.html', {'elementos': elementos})


def bodegas(request):
    if request.method == "POST":
        form = BodegaForm(request.POST)
        if form.is_valid():
            form.save()
    bodegas = Bodega.objects.all()
    form = BodegaForm()
    return render(request, 'bodegas.html', {'bodegas': bodegas, 'formulario': form})

def elementos(request):
    if request.method == "POST":
        form = ElementoForm(request.POST)
        if form.is_valid():
            form.save()
    elementos = Elemento.objects.all()
    form = ElementoForm()
    return render(request, 'elementos.html', {'elementos': elementos, 'formulario': form})


def delete_bodega(request, bodegas):
    if Bodega.objects.filter(id=bodegas).exists():
        Bodega.objects.filter(id=bodegas).delete()
        return redirect('/bodegas/')
    return redirect('/bodegas/')


def update_bodega(request, bodegas):
    bodegas = Bodega.objects.get(id=bodegas)
    update_formulario = BodegaForm(instance=bodegas)
    if request.method == "POST":
        formulario_entrante = BodegaForm(request.POST, instance=bodegas)
        if formulario_entrante.is_valid():
            formulario_entrante.save()
            return redirect('/bodegas/')
    return render(request, "bodega.html", context={"formulario": update_formulario, "bodegas": bodegas})


def bodegas_id(request, id):
    tiene = Tiene.objects.all()
    bodega = Bodega.objects.get(id=id)
    elementos = Elemento.objects.all()
    delegacion = Delegacion.objects.all()
    return render(request, 'bodegax.html', {'bodega': bodega, 'tiene': tiene, 'elementos': elementos, 'delegacion': delegacion})


def delegaciones(request):
    delegaciones = Delegacion.objects.all()
    return render(request, 'delegaciones.html', {'delegaciones': delegaciones})


def entradas(request):
    delegaciones = Delegacion.objects.all()
    bodegas = Bodega.objects.all()

    if request.method == "POST":
        form = TieneForm(request.POST)
        if form.is_valid():
            form.save()
    form = TieneForm()
    return render(request, 'entradas.html', {'delegaciones': delegaciones, 'bodegas': bodegas, 'form': form})


def salidas(request):
    return render(request, 'salidas.html', {})
