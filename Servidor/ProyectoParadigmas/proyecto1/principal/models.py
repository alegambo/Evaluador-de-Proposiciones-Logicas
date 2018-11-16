from django.db import models

# Create your models here.
class Propuesta(models.Model):
	propuesta=models.CharField(max_length=100)
	respuesta=models.CharField(max_length=100,default='lo que sea')
	def __str__(self):
		return self.propuesta