from django import forms
from .models import Course,Category,Tag,Enrollments,Lessons

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'published_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        
class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollments
        fields = '__all__'
        widgets = {
            'enrolled_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'completed_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  
        }

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lessons
        fields = '__all__'