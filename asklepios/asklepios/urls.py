from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls', namespace='login')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('patients/', include('patients.urls', namespace='patients')),
    path('medications/', include('medications.urls', namespace='medications')),
    path('radiology/', include('radiology.urls', namespace='radiology')),
    path('surgeries/', include('surgeries.urls', namespace='surgeries')),
    path('diagnoses/', include('diagnoses.urls', namespace='diagnoses')),
]
