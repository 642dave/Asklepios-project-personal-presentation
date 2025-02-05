from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def patients(request):
    return render(request, 'patients/patients.html')