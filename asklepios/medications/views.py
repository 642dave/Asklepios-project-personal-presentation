from django.shortcuts import render

# Create your views here.
def medications(request):
    return render(request, 'medications/medications.html')