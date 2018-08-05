from django.urls import path
from .views import list_relatorios, create_relatorios, update_relatorio, delete_relatorio

urlpatterns = [
    path('',list_relatorios, name='list_relatorio'),
    path('novo/',create_relatorios, name='create_relatorio'),
    path('alterar/<int:id>/',update_relatorio, name='update_relatorio'),
    path('deletar/<int:id>/',delete_relatorio, name='delete_relatorio'),
]