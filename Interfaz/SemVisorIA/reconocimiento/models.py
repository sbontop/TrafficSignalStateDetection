from django.db import models
from django.utils import timezone

# Create your models here.
class Imagen(models.Model):
    fecha_creacion = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to='')

