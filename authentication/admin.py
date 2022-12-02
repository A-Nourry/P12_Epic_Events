from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):

    list_display = ("id", "first_name", "last_name", "email", "phone", "mobile", "user_team", "password")


admin.site.register(Employee, EmployeeAdmin)
