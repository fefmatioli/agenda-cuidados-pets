from django.shortcuts import render, get_object_or_404, redirect
from .models import Pet, Evento
from .forms import PetForm, EventoForm
from datetime import date
import unicodedata #normalização de texto

def home(request):
    eventos = Evento.objects.filter(data__gte=date.today()).order_by('data')
    pets = Pet.objects.all()
    return render(request, 'agenda/home.html', {
        'eventos': eventos,
        'pets': pets,
    })

def listar_pets(request):
    pets = Pet.objects.all()
    return render(request, 'agenda/listar_pets.html', {'pets': pets})

def adicionar_pet(request):
    form = PetForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listar_pets')
    return render(request, 'agenda/form_pet.html', {'form': form})

def editar_pet(request, id):
    pet = get_object_or_404(Pet, pk=id)
    form = PetForm(request.POST or None, request.FILES or None, instance=pet)
    if form.is_valid():
        form.save()
        return redirect('listar_pets')
    return render(request, 'agenda/form_pet.html', {'form': form})

def remover_pet(request, id):
    pet = get_object_or_404(Pet, pk=id)
    pet.delete()
    return redirect('listar_pets')

def listar_eventos(request):
    eventos = Evento.objects.all().order_by('data')
    return render(request, 'agenda/listar_eventos.html', {'eventos': eventos})

def adicionar_evento(request):
    form = EventoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_eventos')
    return render(request, 'agenda/form_evento.html', {'form': form})

def editar_evento(request, id):
    evento = get_object_or_404(Evento, pk=id)
    form = EventoForm(request.POST or None, instance=evento)
    if form.is_valid():
        form.save()
        return redirect('listar_eventos')
    return render(request, 'agenda/form_evento.html', {'form': form})

def remover_evento(request, id):
    evento = get_object_or_404(Evento, pk=id)
    evento.delete()
    return redirect('listar_eventos')

def remover_acentos(texto):
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')

def buscar(request):
    termo_original = request.GET.get('q', '')
    termo = remover_acentos(termo_original.lower())

    pets = Pet.objects.filter(nome__icontains=termo_original)
    eventos = Evento.objects.filter(
        nome__icontains=termo_original
    ) | Evento.objects.filter(
        tipo__icontains=termo
    ) | Evento.objects.filter(
        pet__nome__icontains=termo_original
    )
    return render(request, 'agenda/busca.html', {'pets': pets, 'eventos': eventos, 'termo': termo_original})
