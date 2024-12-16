from django.contrib import admin
from .models.employee import Employee
from .models.organization import Organization

# Register your models here.

admin.site.register(Employee)
admin.site.register(Organization)
