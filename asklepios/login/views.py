from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import Doctor 

# Create your views here.
def login(request):
    error = None
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        doctor = authenticate(request, email=email, password=password)
        if doctor:
            auth_login(request, doctor)
            return redirect('patients:patients_list')  # Redirection after successful login
        else:
            error = 'Invalid email or password'

    return render(request, 'login/login.html', {'error': error})

def doctors_register(request):
    return render(request, 'login/doctors_register.html')