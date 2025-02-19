from django.shortcuts import render, redirect
from .models import Patient

# Create your views here.
from django.shortcuts import render, redirect
from .models import Patient

def patients_list(request):
    query = request.GET.get('q', '')

    if query:
        patients = Patient.objects.filter(first_name__icontains=query) | Patient.objects.filter(email__icontains=query)
    else:
        patients = []  # Pokud není vyhledávání, tabulka zůstane prázdná

    if request.method == "POST":  # Zpracování formuláře pro přidání pacienta
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        birth_date = request.POST.get("birth_date")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        if first_name and last_name and email and phone:
            Patient.objects.create(
                first_name=first_name,
                last_name=last_name,
                birth_date=birth_date,
                email=email,
                phone=phone
            )
            return redirect('patients:patients_list')  # Obnovení stránky se zaktualizovaným seznamem

    return render(request, 'patients/patients.html', {
        'patients': patients,
        'query': query,
    })


    
