from django.urls import path
from . import views

urlpatterns = [
	path('clients/', views.all_clients, name='all_clients'),
	path('projects/', views.all_projects, name='all_projects'),
]