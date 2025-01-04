from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('accounts/', include('accounts.urls')),
    path('patients/', include('patients.urls')),
    path('medications/', include('medications.urls')),
    path('radiology/', include('radiology.urls')),
    path('surgeries/', include('surgeries.urls')),
    path('diagnoses/', include('diagnoses.urls')),
]
