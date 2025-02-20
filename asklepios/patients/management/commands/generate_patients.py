from django.core.management.base import BaseCommand
from faker import Faker
from patients.models import Patient
import random

fake = Faker()

class Command(BaseCommand):
    help = "Generate 50 fake patients for testing"

    def handle(self, *args, **kwargs):
        gender_choices = ['M', 'F', 'O']

        for _ in range(50):
            birth_number = str(random.randint(100000000, 999999999))  # Generování rodného čísla
            gender = random.choice(gender_choices)
            birth_date = fake.date_of_birth(minimum_age=18, maximum_age=90)  # Generování data narození

            Patient.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                birth_date=birth_date,  # Opraveno, byla tam špatná hodnota
                gender=gender,  # Opraveno, předtím byla chyba
                birth_number=birth_number,  # Opraveno, chyběl čárka v kódu
                address=fake.address(),
                phone=fake.phone_number(),
                email=fake.unique.email()
            )

        self.stdout.write(self.style.SUCCESS('✅ Successfully generated 50 fake patients'))
