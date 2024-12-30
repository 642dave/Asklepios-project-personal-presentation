from django.shortcuts import render

# Create your views here.
def surgeries(request):
    return render(request, 'surgeries/surgeries.html')