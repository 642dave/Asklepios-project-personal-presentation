from django.shortcuts import render, redirect
from .models import Patient

# Create your views here.
from django.shortcuts import render, redirect
from .models import Patient

def patients_list(request):
    query = request.GET.get('q', '')

    if query:
        name_parts = query.split()
        filters = Patient.objects.none()

        for part in name_parts:
            filters |= Patient.objects.filter(first_name__icontains=part)
            filters |= Patient.objects.filter(last_name__icontains=part)
            filters |= Patient.objects.filter(email__icontains=part)

        patients = filters.distinct()
    else:
        patients = []

    # 💡 Definujeme prázdné proměnné pro případ, že request není POST
    first_name = last_name = birth_number = birth_date = gender = address = email = phone = ""

    if request.method == "POST":  # Zpracování formuláře pro přidání pacienta
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        birth_number = request.POST.get("birth_number", "").strip()
        birth_date = request.POST.get("birth_date", "").strip()
        gender = request.POST.get("gender", "").strip()
        address = request.POST.get("address", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()

        if first_name and last_name and birth_number and birth_date and gender and address and email and phone:
            Patient.objects.create(
                first_name=first_name,
                last_name=last_name,
                birth_number=birth_number,
                birth_date=birth_date,
                gender=gender,
                address=address,
                email=email,
                phone=phone
            )
            return redirect('patients:patients_list')  # Obnovení stránky se zaktualizovaným seznamem
        else:
            print("❌ Některé pole nebylo vyplněno!")

    return render(request, 'patients/patients.html', {
        'patients': patients,
        'query': query,
    })


    
