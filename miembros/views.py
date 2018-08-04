from django.shortcuts import render, redirect
from django.views.generic import View 
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.urlresolvers import reverse_lazy

from .models import Miembro
from .forms import MiembroForm
from core.utils import load_miembros

# ==================================================
# Mixins
# ==================================================

class MiembroMixin(LoginRequiredMixin):
	model = Miembro
	success_url = reverse_lazy('miembros:list')


class MiembroEditMixin(MiembroMixin, PermissionRequiredMixin):
	template_name = 'miembros/edit.html'
	form_class = MiembroForm
	permission_required = ('miembros.can_add', 'miembros.can_edit')


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


class MiembrosUpdateView(MiembroEditMixin, UpdateView):
	pass


#"""
# Sólo se utiliza una vez
class CargaUsuarios(View):

	def get(self, request, *args, **kwargs):
		print()
		print('*'*50)
		print('Executing load users ...')
		print('*'*50)
		print()

		load_miembros()
		return redirect('miembros:list')
#"""