from django.shortcuts import render

# Create your views here.
def diagnoses(request):
    return render(request, 'diagnoses/diagnoses.html')