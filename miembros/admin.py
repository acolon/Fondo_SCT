from django.contrib import admin

from .models import Banco, Miembro

# ==================================================
# Admin Registrations
# ==================================================

@admin.register(Banco)
class BancoAdmin(admin.ModelAdmin):
	list_display  = [ 'nombre' ]
	search_fields = [ 'nombre' ]


@admin.register(Miembro)
class MiembroAdmin(admin.ModelAdmin):
	list_display  = [ 'nombre', 'email', 'cuenta', 'banco', 
			'fecha_nac', 'fecha_ing', 'activo'
			]
	search_fields = [ 'nombre' ]

