from django.urls import path
from . import views

# registered application name
app_name = 'radiology' 

urlpatterns = [
    path('radiology/', views.radiology, name='radiology')
]
