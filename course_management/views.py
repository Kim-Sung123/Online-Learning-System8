from django.shortcuts import render,redirect,get_object_or_404
from .models import Course,Category,Tag,Enrollments,Lessons
from .forms import CourseForm,CategoryForm,TagForm,EnrollmentForm,LessonForm
from users.decorators import login_required, student_required, instructor_required, employee_required

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

@employee_required
def course_add(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('course_list')
    return render(request, 'courses/course_add.html', {'form': form})

@employee_required
def course_edit(request,pk):
    course = Course.objects.filter(pk=pk).first()
    form = CourseForm(request.POST or None,instance=course)
    if form.is_valid():
        form.save()
        return redirect('course_list')
    return render(request, 'courses/course_edit.html', {'form': form})

@employee_required
def course_delete(request,pk):
    course = Course.objects.filter(pk=pk).first()
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'courses/course_delete.html', {'course': course})

# category
@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})
@employee_required
def category_add(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'categories/category_add.html', {'form': form})

@employee_required
def category_edit(request, pk):
    category = Category.objects.filter(pk=pk).first()
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'categories/category_edit.html', {'form': form})

@employee_required
def category_delete(request, pk):
    category = Category.objects.filter(pk=pk).first()
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'categories/category_delete.html', {'category': category})

# tags
@login_required 
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags/tag_list.html', {'tags': tags})

@employee_required
def tag_add(request):
    form = TagForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tag_list')
    return render(request, 'tags/tag_add.html', {'form': form})

@employee_required
def tag_edit(request, pk):
    tag = Tag.objects.filter(pk=pk).first()
    form = TagForm(request.POST or None, instance=tag)
    if form.is_valid():
        form.save()
        return redirect('tag_list')
    return render(request, 'tags/tag_edit.html', {'form': form})

@employee_required
def tag_delete(request, pk):
    tag = Tag.objects.filter(pk=pk).first()
    if request.method == 'POST':
        tag.delete()
        return redirect('tag_list')
    return render(request, 'tags/tag_delete.html', {"tag":tag})

# enrollment

@login_required
def enrollment_list(request):
    enrollments = Enrollments.objects.all()
    return render(request,"enrollments/enrollment_list.html",{"enrollments":enrollments})
@employee_required
def enrollment_add(request):
    form = EnrollmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("enrollment_list")
    return render(request,"enrollments/enrollment_add.html",{"form":form})
@employee_required
def enrollment_edit(request,pk):
    enrollment = get_object_or_404(Enrollments,pk=pk)
    form = EnrollmentForm(request.POST or None, instance=enrollment)
    if form.is_valid():
        form.save()
        return redirect("enrollment_list")
    return render(request,"enrollments/enrollment_edit.html",{"form":form})
@employee_required
def enrollment_delete(request,pk):
    enrollment = get_object_or_404(Enrollments,pk=pk)
    if request.method == 'POST':
        enrollment.delete()
        return redirect("enrollment_list")
    return render(request,"enrollments/enrollment_delete.html",{"enrollment":enrollment})

# lesson
@login_required
def lesson_list(request):
    lessons = Lessons.objects.all()
    return render(request, 'lessons/lesson_list.html', {'lessons': lessons})

@employee_required
def lesson_add(request):
    form = LessonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lesson_list")
    return render (request,"lessons/lesson_add.html",{"form":form})
@employee_required
def lesson_edit(request,pk):
    lesson = Lessons.objects.filter(pk=pk).first()
    form = LessonForm(request.POST or None,instance=lesson)
    if form.is_valid():
        form.save()
        return redirect("lesson_list")
    return render (request,"lessons/lesson_edit.html",{"form":form})
@employee_required
def lesson_delete(request,pk):
    lesson = Lessons.objects.filter(pk=pk).first()
    if request.method == 'POST':
        lesson.delete()
        return redirect("lesson_list")
    return render (request,"lessons/lesson_delete.html",{"lesson":lesson})
    