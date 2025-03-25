from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from faker import Faker
import random
from login.models import Doctor

class Command(BaseCommand):
    help = "Generate fake doctors for testing"

    def handle(self, *args, **kwargs):
        fake = Faker()
        specialization = [
            "Cardiology", "Neurology", "Oncology", 
            "Pediatrics", "Psychiatry", "Radiology", 
            "General Medicine", "Dermatology"
        ]

        for _ in range(30):
            Doctor.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                password=make_password('Test1234'),  # Default password
                specialization=random.choice(specialization)
            )

        self.stdout.write(self.style.SUCCESS('✅ Successfully generated 30 fake doctors'))