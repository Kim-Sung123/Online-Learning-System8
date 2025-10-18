from django.db import models
from users.models import Instructor,Student

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
class Course(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True) 
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft', null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    duration_hours = models.PositiveIntegerField(default=0, null=True)
    
    def __str__(self):
        return self.title
    
    
class Lessons(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True )
    title = models.CharField(max_length=200,null=True)
    video_url = models.URLField(blank=True,null=True)
    video_file = models.FileField(upload_to='lesson_videos/', null=True, blank=True)
    document = models.FileField(upload_to='lesson_documents/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.course.title} - {self.title}"
    

class Enrollments(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments', null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments', null=True)
    enrolled_date = models.DateTimeField(auto_now_add=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    
    def __str__(self):
        return f"{self.student.name} - {self.course.title}"
