from django.urls import path
from . import views

urlpatterns = [
    path('surgeries/', views.surgeries, name='surgeries')
]
