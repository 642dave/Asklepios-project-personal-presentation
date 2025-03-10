from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import Doctor 

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        doctor = authenticate(request, email=email, password=password)
        if doctor:
            auth_login(request, doctor)
            return redirect('patients:patients_list')  # Redirection after successful login
        else:
            messages.error(request, 'Invalid email or password')  # Použijeme messages pro výpis chyb
        
        return redirect('login:login')  # Přesměrování pro nový CSRF token

    return render(request, 'login/login.html')

def doctors_register(request):
    return render(request, 'login/doctors_register.html')
