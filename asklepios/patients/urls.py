from django.urls import path
from . import views

# registered application name
app_name = 'patients' 

urlpatterns = [
    path('', views.patients_list, name='patients_list'),
]
