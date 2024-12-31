from django.urls import path
from . import views

urlpatterns = [
    path('', views.diagnoses, name='diagnoses')
]
