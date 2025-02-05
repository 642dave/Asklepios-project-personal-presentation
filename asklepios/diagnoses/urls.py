from django.urls import path
from . import views

# registered application name
app_name = 'diagnoses' 

urlpatterns = [
    path('diagnoses/', views.diagnoses, name='diagnoses')
]
