from django import forms
from .models import Pet, Evento

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'
