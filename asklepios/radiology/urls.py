from django.urls import path
from . import views

# registered application name
app_name = 'radiology' 

urlpatterns = [
    path('', views.radiology, name='radiology')
]
