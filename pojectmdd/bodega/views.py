from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import BodegueroForm, BodegaForm, TieneForm, DelegacionForm
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
    if request.method == "POST":
        form = DelegacionForm(request.POST)
        if form.is_valid():
            form.save()
    delegaciones = Delegacion.objects.all()
    form = DelegacionForm()
    return render(request, 'delegaciones.html', {'delegaciones': delegaciones, 'formulario': form})

def delete_delegacion(request, delegaciones):
    if Delegacion.objects.filter(id=delegaciones).exists():
        Delegacion.objects.filter(id=delegaciones).delete()
        return redirect('/delegaciones/')
    return redirect('/delegaciones/')


def update_delegacion(request, delegaciones):
    delegaciones = Delegacion.objects.get(id=delegaciones)
    update_formulario = DelegacionForm(instance=delegaciones)
    if request.method == "POST":
        formulario_entrante = DelegacionForm(request.POST, instance=delegaciones)
        if formulario_entrante.is_valid():
            formulario_entrante.save()
            return redirect('/delegaciones/')
    return render(request, "delegacion.html", {"formulario": update_formulario, "delegaciones": delegaciones})

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
