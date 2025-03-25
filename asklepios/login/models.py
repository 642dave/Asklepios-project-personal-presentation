from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class DoctorManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Doctor must have an email address')
        email = self.normalize_email(email)
        doctor = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        doctor.set_password(password)  # Password hashing
        doctor.save(using=self._db)
        return doctor
        
    def create_superuser(self, email, first_name, last_name, password):
        doctor = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        doctor.is_admin = True
        doctor.save(using=self._db)
        return doctor
    
# Custom model for doctors
class Doctor(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    specialization = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = DoctorManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def is_staff(self):
        return self.is_admin 