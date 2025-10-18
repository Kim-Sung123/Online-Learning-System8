from django.contrib import admin
from .models import Student,Instructor,Employee,User

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Employee)