from django.urls import path
from . import views

urlpatterns = [
	path('projects/', views.all_projects, name='all_projects'),
]