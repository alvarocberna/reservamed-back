from django.db import models
from profesion.models import Profesion

class Profesional(models.Model):
    # choices
    class Sexo(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMENINO = 'F', 'Femenino'
        OTRO = 'O', 'Otro'

    rut_profesional = models.CharField(max_length=10)
    profesion = models.ForeignKey(Profesion, on_delete=models.SET_NULL, null=True, db_column='profesion')
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30, null=True)
    ap_paterno = models.CharField(max_length=30)
    ap_materno = models.CharField(max_length=30, null=True)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=Sexo.choices)
    correo = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'profesional'