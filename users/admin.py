from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CunaUserCreationForm, CunaUserChangeForm
from .models import CunaUser

# ==================================================
# ==================================================

class CunaUserAdmin(UserAdmin):
	add_form = CunaUserCreationForm
	form = CunaUserChangeForm
	model = CunaUser
	list_display = [ 'username', 'email', 'miembro' ]
	search_fields = [ 'username', 'email' ]

	fieldsets = (
		('User Information', {'fields': (
			'miembro', )}),
		) + UserAdmin.fieldsets

admin.site.register(CunaUser, CunaUserAdmin)