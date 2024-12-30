from django.urls import path
from . import views

urlpatterns = [
    path('radiology/', views.radiology, name='radiology')
]
