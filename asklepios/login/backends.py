from django.contrib.auth.backends import BaseBackend
from .models import Doctor

class DoctorAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            doctor = Doctor.objects.get(email=email)
            if doctor.check_password(password):  # Password verification using AbstractBaseUser
                return doctor
        except Doctor.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Doctor.objects.get(pk=user_id)
        except Doctor.DoesNotExist:
            return None