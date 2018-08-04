from django.contrib import admin

# ==================================================
# Admin Mixins
# ==================================================

class BasicListAdmin(object):
	list_display = [ 'descripcion' ]
	search_fields = [ 'descripcion' ]


