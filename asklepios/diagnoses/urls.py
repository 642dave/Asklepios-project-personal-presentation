from django.urls import path
from . import views

# registered application name
app_name = 'diagnoses' 

urlpatterns = [
    path('', views.diagnoses, name='diagnoses')
]
