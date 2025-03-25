from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]

    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    birth_date = models.DateField(verbose_name='Date of birth')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Gender')

    birth_number = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Birth Number',
        validators=[RegexValidator(r'^\d{9,12}$', 'Personal ID must be 9-12 digits')],
    )
    

    address = models.TextField(verbose_name='Address')
    phone = models.CharField(max_length=30, unique=True, verbose_name='Phone Number')
    email = models.EmailField(unique=True, verbose_name='Email')
    registered_at = models.DateTimeField(auto_now_add=True, verbose_name='Registered At')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.personal_id})"



