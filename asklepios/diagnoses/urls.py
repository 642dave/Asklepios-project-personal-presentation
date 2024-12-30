from django.urls import path
from . import views

urlpatterns = [
    path('diagnoses/', views.diagnoses, name='diagnoses')
]
