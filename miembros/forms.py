from django import forms
from bootstrap_datepicker_plus import DatePickerInput

from .models import Miembro

class MiembroForm(forms.ModelForm):

	#'''
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['fecha_nac'].widget = DatePickerInput(format='%Y-%m-%d')
		self.fields['fecha_nac'].required = False

		self.fields['fecha_ing'].widget = DatePickerInput(format='%Y-%m-%d')
		self.fields['fecha_ing'].required = False

		self.fields['cuenta'].required = False
		self.fields['banco'].required = False
	#'''

	class Meta:
		model = Miembro

		fields = [ 'nombre', 'email',  'fecha_nac', 
			'fecha_ing', 'cuenta', 'banco' ]

	'''
	nombre	
	email	
	cuenta	
	banco	
	fecha_nac
	fecha_ing
	activo	
	#'''

