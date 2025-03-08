from django.urls import path
from . import views

app_name = 'medical_records'

urlpatterns = [
    path('medications/', views.medications, name='medications'),
    path('radiology/', views.radiology, name='radiology'),
    path('surgeries/', views.surgeries, name='surgeries'),
]
