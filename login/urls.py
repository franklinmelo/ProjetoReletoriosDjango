from django.contrib import admin
from django.urls import path, include
from login import views



urlpatterns = [
    path('formulario/', include('formulario.urls')),
    path('', views.index, name='index')
    
    
]