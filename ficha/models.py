from django.db import models
from profesional.models import Profesional
from paciente.models import Paciente

class Ficha(models.Model):
    # si se elimina al profesional, se elimina la ficha
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, null=True, db_column='profesional')
    # si se elimina al paciente, se deja la ficha con el paciente en null
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True, db_column='paciente')
    descripcion = models.CharField(max_length=300, null=True)
    diagnostico = models.CharField(max_length=300, null=True)
    tratamiento = models.CharField(max_length=300, null=True)
    fecha_ingreso = models.DateField()
    fecha_control = models.DateTimeField(null=True)

    class Meta:
        db_table = 'ficha'