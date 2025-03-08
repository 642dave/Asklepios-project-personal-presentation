from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls', namespace='login')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('patients/', include('patients.urls', namespace='patients')),
    path('medical-records/', include('medical_records.urls', namespace='medical_records')),
    path('diagnoses/', include('diagnoses.urls', namespace='diagnoses')),
]
