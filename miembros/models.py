from django.db import models
from django.conf import settings

# ==================================================
# Model Managers
# ==================================================

class MiembroManager(models.Manager):

	def activos(self):
		qs = self.filter(activo=True)
		return qs

	def sin_confirmar(self):
		qs = self.filter(usuario=Null)
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
	nombre			= models.CharField(max_length=50)
	apellido		= models.CharField(max_length=50)
	email			= models.EmailField()
	cuenta			= models.CharField(max_length=50)
	banco			= models.ForeignKey(Banco, on_delete=models.PROTECT)
	fecha_ingreso	= models.DateField()
	username		= models.CharField(max_length=50)
	activo			= models.BooleanField(default=True)
	usuario			= models.ForeignKey(
							settings.AUTH_USER_MODEL, 
							blank=True,
							null=True)

	@property
	def configurado(self):
		r = 'No'
		if self.usuario:
			r = 'Si'
		return r

	objects = MiembroManager()
	
	def __str__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		self.nombre = self.nombre.strip().title()
		self.apellido = self.apellido.strip().title()
		self.email = self.email.strip().lower()
		self.username = self.username.strip().lower()
		super(Miembro, self).save(*args, **kwargs)

	class Meta:
		ordering=['nombre']

