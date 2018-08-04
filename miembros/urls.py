from django.conf.urls import url
from . import views 

urlpatterns = [

	url(r'^$', 
		views.MiembrosListView.as_view(), 
		name='list'), 
	
	url(r'^nuevo/$', 
		views.MiembrosCreateView.as_view(), 
		name='add'), 

	url(r'^(?P<pk>\d+)/edit/$', 
		views.MiembrosUpdateView.as_view(), 
		name='edit'), 
	

	url(r'^carga/$', 
		views.CargaUsuarios.as_view(), 
		name='carga'), 

	]

"""
	url(r'^carga/$', 
		views.CargaUsuarios.as_view(), 
		name='carga'), 
	
"""