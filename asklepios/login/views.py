from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login/login.html')

def doctors_register(request):
    return render(request, 'login/doctors_register.html')