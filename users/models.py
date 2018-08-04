from django.db import models
from django.contrib.auth.models import AbstractUser

from miembros.models import Miembro 

# ==================================================
# ==================================================

class CunaUser(AbstractUser):

	miembro = models.ForeignKey(Miembro, null=True, 
				on_delete=models.SET_NULL,
				related_name='user')

	def __str__(self):
		r = self.username
		if self.miembro:
			r = self.miembro.nombre
		return r
