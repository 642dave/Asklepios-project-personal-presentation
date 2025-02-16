from django.core.management.base import BaseCommand
from faker import Faker
from patients.models import Patient
import random

class Command(BaseCommand):
    help = "Generate fake patients for testing"

    def handle(self, *args, **kwargs):
        fake = Faker()
        gender_choices = ['M', 'F', 'O']

        for i in range(50):
            Patient.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                birth_date=fake.date_of_birth(minimum_age=18, maximum_age=90),
                gender=random.choice(gender_choices),
                personal_id=fake.unique.random_number(digits=10, fix_len=True),
                address=fake.address(),
                phone=fake.unique.phone_number(),
                email=fake.unique.email()
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated 50 fake patients'))