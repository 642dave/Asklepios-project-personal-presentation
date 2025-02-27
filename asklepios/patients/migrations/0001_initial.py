# Generated by Django 4.2.19 on 2025-02-20 16:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('birth_date', models.DateField(verbose_name='Date of birth')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1, verbose_name='Gender')),
                ('birth_number', models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^\\d{9,12}$', 'Personal ID must be 9-12 digits')], verbose_name='Birth Number')),
                ('address', models.TextField(verbose_name='Address')),
                ('phone', models.CharField(max_length=30, unique=True, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('registered_at', models.DateTimeField(auto_now_add=True, verbose_name='Registered At')),
            ],
        ),
    ]
