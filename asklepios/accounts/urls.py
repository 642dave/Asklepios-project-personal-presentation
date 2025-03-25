from django.urls import path
from . import views

# registered application name
app_name = 'accounts' 

urlpatterns = [
    path('', views.accounts, name='accounts'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy')
]
