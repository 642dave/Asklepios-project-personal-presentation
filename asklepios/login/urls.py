from django.urls import path
from . import views

# registered application name
app_name = 'login' 

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('doctors-register/', views.doctors_register, name='doctors-register'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy')
]
