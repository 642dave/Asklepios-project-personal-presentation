from django.urls import path
from . import views

# registered application name
app_name = 'medications' 

urlpatterns = [
    path('medications/', views.medications, name='medications')
]
