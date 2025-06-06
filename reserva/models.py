from django.db import models
from profesional.models import Profesional
from paciente.models import Paciente

class Reserva(models.Model):
    class EstadoReserva(models.TextChoices):
        PENDIENTE = 'Pendiente', 'Pendiente'
        CONFIRMADA = 'Confirmada', 'Confirmada'
        CANCELADA = 'Cancelada', 'Cancelada'

    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, db_column='profesional')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='paciente')
    fecha_reserva = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=EstadoReserva.choices, default=EstadoReserva.PENDIENTE)

    class Meta:
        db_table = 'reserva'