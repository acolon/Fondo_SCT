from django.contrib.auth.models import User
import string, random

from miembros.models import Banco, Miembro 

class UserInfo():

	usename = ''
	first_name = ''
	last_name = ''
	email = ''

	def __init__(self, arr):
		self.username = arr[0].lower()
		self.first_name = arr[1].title()
		self.last_name = arr[2].title()
		self.email = arr[3]

class MiembroInfo():

	nombre = ''
	email  = ''
	cuenta = ''

	def __init__(self, arr):
		self.nombre = arr[0].strip().title()
		self.email  = arr[1].strip().lower()
		self.cuenta = arr[2].strip()


def gen_pwd():
	a = string.ascii_letters
	b = string.digits
	c = string.punctuation
	c = c.replace('"', '').replace("'", "")
	c = c.replace('\\', '').replace('`', '')
	c = c.replace('#', '').replace('{','')
	c = c.replace('}', '')
	d = a + b + c

	r = ''.join([random.choice(d) for i in range(16)])
	return r


def load_miembros():

	arr = []

	'''
	arr.append(('dahiana', 'Dahiana.Paulino@quadpackaging.com', '779547777'))
	arr.append(('Juan Amaury vasquez', 'juanamaury@gmail.com', '791103112'))
	arr.append(('Andres Germán', '<pendiente>', '751541129'))
	arr.append(('Annya Medrano', '<pendiente>', '748457280'))
	arr.append(('Victor Cocco', 'vcoccomedina@gmail.com', '803376532'))
	arr.append(('David Sanchez', '<pendiente>', '728562497'))
	arr.append(('Sucre Brens', 'sucrebrens@gmail.com', '725268080'))
	arr.append(('Maria Chevalier', 'cheva78@hotmail.com', '702483348'))
	arr.append(('marlenne Ruiz', 'mm.marlenneruiz@gmail.com', '2610013835'))
	arr.append(('jaissa fernandez', '<pendiente>', '719042806'))
	arr.append(('ramiro sanchez', 'ramiroenrique@gmail.com', '804782951'))
	arr.append(('michael nakasu', 'nakasu@hotmail.com', '')) 
	arr.append(('jose cocco', 'joco45@hotmail.com', ''))
	arr.append(('Jeffrey Tello', 'jtellog89@gmail.com', ''))
	#'''

	'''
	nombre	
	email	
	cuenta	
	banco	
	fecha_nac
	fecha_ing
	activo	
	#'''

	for c in arr:

		m = MiembroInfo(c)

		Miembro.objects.create(
			nombre 		= m.nombre,
			email 		= m.email,
			cuenta 		= m.cuenta,
			)

