from django.db import models

# Create your models here.


class Mascota(models.Model):
	nombre = models.CharField(max_length=50)
	sexo = models.CharField(max_length=10)
	edad = models.IntegerField()
	edad = models.IntegerField()
	fecha_recate = models.DateField()	


