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

	username = ''
	cuenta = ''
	nombre_banco = ''

	user = None
	banco = None

	def __init__(self, arr):
		self.username = arr[0].lower()
		self.cuenta = arr[1]
		self.nombre_banco = arr[2]

		try:
			self.user = User.objects.get(username=self.username)
		except:
			self.user = None

		try:
			self.banco = Banco.objects.get(nombre=self.nombre_banco)
		except:
			self.banco = None

	@property
	def is_valid(self):
		r = False
		if self.user:
			r = True
		return r
	

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


def load_users():

	users = []
	users.append(('ramiro', 'ramiro', 'sanchez', 'ramiroenrique@gmail.com'))
	users.append(('amaury', 'juan amaury', 'vasquez', 'juanamaury@gmail.com'))
	users.append(('nakasu', 'Michael', 'Nakasu', 'nakasu@hotmail.com')) 
	users.append(('marlenne', 'Marlenne', 'Ruiz', 'mm.marlenneruiz@gmail.com'))
	users.append(('victor', 'Victor', 'Cocco', 'vcoccomedina@gmail.com'))
	users.append(('cocco', 'jose', 'cocco', 'joco45@hotmail.com'))
	users.append(('maria', 'maria', 'chevalier', 'cheva78@hotmail.com'))
	users.append(('jeffrey', 'Jeffrey', 'Tello', 'jtellog89@gmail.com'))
	users.append(('sucre', 'Sucre', 'Brens', 'sucrebrens@gmail.com'))
	users.append(('dahiana', 'dahiana', 'Paulino', 'Dahiana.Paulino@quadpackaging.com'))

	for u in users:
		o = UserInfo(u)
		p = gen_pwd()
		User.objects.create_user(o.username, o.email, p, 
			first_name = o.first_name,
			last_name  = o.last_name
			)


def load_miembros():
	arr = []
	#arr.append(('dahiana', 	'779547777', 	'Popular'))
	#arr.append(('amaury', 	'791103112', 	'Popular'))
	arr.append(('andres', 	'751541129', 	'Popular'))
	arr.append(('annya', 	'748457280', 	'Popular'))
	arr.append(('victor', 	'803376532', 	'Popular'))
	arr.append(('david', 	'728562497', 	'Popular'))
	arr.append(('sucre', 	'725268080', 	'Popular'))
	arr.append(('maria', 	'702483348', 	'Popular'))
	arr.append(('marlenne', 	'2610013835', 	'Reservas'))
	arr.append(('jaissa', 	'719042806', 	'Popular'))
	arr.append(('ramiro', 	'804782951', 	'Popular'))

	for c in arr:

		m = MiembroInfo(c)

		first_name = '.'
		last_name = '.'
		email = '.'
		
		if m.is_valid:
			first_name 	= m.user.first_name
			last_name  	= m.user.last_name
			email 		= m.user.email
		
		Miembro.objects.create(
			nombre 		= first_name,
			apellido 	= last_name,
			email 		= email,
			username	= m.username,
			cuenta 		= m.cuenta,
			banco 		= m.banco,
			fecha_ingreso = '2014-10-30',
			usuario 	= m.user
			)

