from django.shortcuts import render

# Create your views here.
def radiology(request):
    return render(request, 'radiology/radiology.html')