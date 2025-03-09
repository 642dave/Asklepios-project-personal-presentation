from django.contrib import admin

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'specialization', 'is_active')
    search_fields = ('first_name', 'last_name', 'email', 'specialization')
    list_filter = ('is_active', 'specialization')