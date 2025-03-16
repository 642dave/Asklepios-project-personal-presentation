from django.urls import path
from . import views

# registered application name
app_name = 'login' 

urlpatterns = [
    path('', views.login, name='login'),
    path('doctors_register/', views.doctors_register, name='doctors-register'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy')
]
