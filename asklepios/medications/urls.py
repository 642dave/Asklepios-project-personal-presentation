from django.urls import path
from . import views

urlpatterns = [
    path('', views.medications, name='medications')
]
