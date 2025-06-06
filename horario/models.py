from django.db import models
from profesional.models import Profesional

class Horario(models.Model):
    class Dias(models.TextChoices):
        LUNES = 'LU', 'Lunes'
        MARTES = 'MA', 'Martes'
        MIERCOLES = 'MI', 'Miercoles'
        JUEVES = 'JU', 'Jueves'
        VIERNES = 'VI', 'Viernes'
        SABADO = 'SA', 'Sabado'
        DOMINGO = 'DO', 'Domingo'

    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, db_column='profesional')
    dia = models.CharField(max_length=2, choices=Dias.choices)
    hora_inicio = models.DateTimeField()
    hora_fin = models.DateTimeField()

    class Meta:
        db_table = 'horario'