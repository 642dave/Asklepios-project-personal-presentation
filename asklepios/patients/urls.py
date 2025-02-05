from django.urls import path
from . import views

# registered application name
app_name = 'patients' 

urlpatterns = [
    path('patients/', views.patients, name='patients')
]
