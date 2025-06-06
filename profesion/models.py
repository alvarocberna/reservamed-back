from django.db import models

# Create your models here.

class Profesion(models.Model):
    
    descripcion = models.CharField(max_length=50)

    class Meta:
        db_table = 'profesion'