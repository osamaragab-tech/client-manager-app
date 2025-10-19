from django.contrib import admin
from django.urls import path
from clients import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.client_list, name='client_list'),
    path('edit/<int:pk>/', views.edit_client, name='edit_client'),
    path('delete/<int:pk>/', views.delete_client, name='delete_client'),
    path('export_excel/', views.export_clients_excel, name='export_clients_excel'),

]
