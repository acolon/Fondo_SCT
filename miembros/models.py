from django.db import models
from django.conf import settings

# ==================================================
# Model Managers
# ==================================================

class MiembroManager(models.Manager):

	def activos(self):
		qs = self.filter(activo=True)
		return qs


# ==================================================
# Model Classes
# ==================================================

class Banco(models.Model):
	nombre	= models.CharField(max_length=50)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering=['nombre']


class Miembro(models.Model):
	nombre		= models.CharField(max_length=100)
	email		= models.EmailField()
	cuenta		= models.CharField(max_length=50, blank=True)
	banco		= models.ForeignKey(Banco, null=True, on_delete=models.SET_NULL)
	fecha_nac	= models.DateField(null=True)
	fecha_ing	= models.DateField(null=True)
	activo		= models.BooleanField(default=True)

	objects = MiembroManager()
	
	def __str__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		self.nombre = self.nombre.strip().title()
		self.email = self.email.strip().lower()
		super(Miembro, self).save(*args, **kwargs)

	class Meta:
		ordering=['nombre']
		

