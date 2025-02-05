from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('', include('accounts.urls')),
    path('', include('patients.urls')),
    path('', include('medications.urls')),
    path('', include('radiology.urls')),
    path('', include('surgeries.urls')),
    path('', include('diagnoses.urls')),
]
