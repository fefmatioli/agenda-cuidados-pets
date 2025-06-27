from django.db import models

class Pet(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    especie = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='pets/')

    def __str__(self):
        return self.nome

class Evento(models.Model):
    TIPOS = [
        ('banho', 'Banho'),
        ('vacina', 'Vacina'),
        ('consulta', 'Consulta'),
        ('remedio', 'Remédio'),
    ]

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='eventos')
    tipo = models.CharField(max_length=20, choices=TIPOS)
    data = models.DateTimeField()

    def __str__(self):
        return f'{self.get_tipo_display()} - {self.pet.nome} ({self.data})'
