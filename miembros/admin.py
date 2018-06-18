from django.contrib import admin

from .models import Banco, Miembro

# ==================================================
# Admin Mixins
# ==================================================

class BasicListAdmin(object):
	list_display = [ 'descripcion' ]
	search_fields = [ 'descripcion' ]


# ==================================================
# Admin Registrations
# ==================================================

@admin.register(Banco)
class BancoAdmin(admin.ModelAdmin):
	list_display  = [ 'nombre' ]
	search_fields = [ 'nombre' ]


@admin.register(Miembro)
class MiembroAdmin(admin.ModelAdmin):
	list_display  = [ 
			'nombre', 'apellido', 'email', 'cuenta', 
			'banco', 'fecha_ingreso', 'username', 
			'activo', 'usuario'
			]
	search_fields = [ 'nombre', 'apellido' ]

