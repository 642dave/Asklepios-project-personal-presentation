from django.shortcuts import render

# Create your views here.

# Medications view
def medications(request):
    return render(request, 'medical_records/medications.html')

# Radiology views
def radiology(request):
    return render(request, 'medical_records/radiology.html')

# Surgeries views
def surgeries(request):
    return render(request, 'medical_records/surgeries.html')