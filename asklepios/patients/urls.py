from django.urls import path
from . import views

# registered application name
app_name = 'patients' 

urlpatterns = [
    path('', views.patients_list, name='patients_list'),
    path('delete/<int:patient_id>/', views.delete_patient, name='delete_patient')
]
