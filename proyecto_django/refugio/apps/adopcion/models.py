from django.db import models

# Create your models here.

class Persona(models.Model):
	legajo = models.CharField(max_length=10,primary_key=True)
	nombre = models.CharField(max_length=25)
	appelidos = models.CharField(max_length=25)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=12)
	email = models.EmailField()
	direccion_domiciolio = models.TextField()
