from django.contrib import admin
from my_crud_app.models import Student

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'address', 'phone', 'email', 'password')