from django.shortcuts import render, redirect
from django.views.generic import View 
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

from .models import Miembro
from core.utils import load_users, load_miembros

# ==================================================
# Mixins
# ==================================================

class MiembroMixin(LoginRequiredMixin):
	model = Miembro
	success_url = reverse_lazy('miembros:list')


class MiembroEditMixin(MiembroMixin):
	template_name = 'miembros/edit.html'
	fields = [ 'nombre', 'apellido', 'email', 'fecha_ingreso', 
			'cuenta', 'banco', 'username' ]


# ==================================================
# Clientes Views
# ==================================================

class MiembrosListView(MiembroMixin, ListView):
	template_name = 'miembros/list.html'

	def get_queryset(self):
		qs = Miembro.objects.activos()
		return qs


class MiembrosCreateView(MiembroEditMixin, CreateView):
	pass


"""
# Sólo se utiliza una vez
class CargaUsuarios(View):

	def get(self, request, *args, **kwargs):
		print()
		print('*'*50)
		print('Executing load users ...')
		print('*'*50)
		print()

		#load_users()
		load_miembros()
		return redirect('miembros:list')
"""