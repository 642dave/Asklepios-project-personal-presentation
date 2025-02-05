from django.urls import path
from . import views

# registered application name
app_name = 'login' 

urlpatterns = [
    path('', views.login, name='login'),
]
