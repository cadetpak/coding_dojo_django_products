from django.conf.urls import patterns, url 
from . import views

urlpatterns = [
	url(r'^products$', views.index, name='index'),
	url(r'^add_product$', views.add, name='add'),
	url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
	url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
	url(r'^update/(?P<id>\d+)$', views.update, name='update'),
]