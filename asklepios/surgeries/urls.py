from django.urls import path
from . import views

# registered application name
app_name = 'surgeries' 

urlpatterns = [
    path('', views.surgeries, name='surgeries')
]
