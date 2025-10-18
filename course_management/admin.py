from django.contrib import admin
from .models import Course,Category,Tag,Enrollments,Lessons

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Lessons)
admin.site.register(Enrollments)