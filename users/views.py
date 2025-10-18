from itertools import count
from django.shortcuts import render,redirect,get_object_or_404
from .models import Student,Instructor,Employee,User
from .forms import StudentForm,InstructorForm,EmployeeForm,RegisterForm
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from .decorators import *
from django.db.models import Count, Q
from django.utils import timezone
from users.decorators import login_required, student_required, instructor_required, employee_required

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request,"students/student_list.html",{"students":students})

@employee_required
def student_add(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("student_list")
    return render(request,"students/student_add.html",{"form" :form})

@employee_required
def student_edit(request,pk):
    student = Student.objects.filter(pk=pk).first()
    form = StudentForm(request.POST or None,instance=student)
    if form.is_valid():
        form.save()
        return redirect("student_list")
    return render(request,"students/student_edit.html",{"form" :form})

@employee_required
def student_delete(request,pk):
    student = Student.objects.filter(pk=pk).first()
    if request.method == "POST":
        student.delete()
        return redirect("student_list")
    return render(request,"students/student_delete.html",{"student" : student})
        
# instructors
@login_required
def instructor_list(request):
    instructors = Instructor.objects.all()
    return render (request,"instructors/instructor_list.html",{"instructors":instructors})

@employee_required
def instructor_add(request):
    form = InstructorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("instructor_list")
    return render(request,"instructors/instructor_add.html",{"form":form})

@employee_required
def instructor_edit(request,pk):
    instructor = Instructor.objects.filter(pk=pk).first()
    form = InstructorForm(request.POST or None, instance=instructor)
    if form.is_valid():
        form.save()
        return redirect("instructor_list")
    return render(request,"instructors/instructor_edit.html",{"form":form})

@employee_required
def instructor_delete(request,pk):
    instructor = Instructor.objects.filter(pk=pk).first()
    if request.method == 'POST':
        instructor.delete()
        return redirect("instructor_list")
    return render(request,"instructors/instructor_delete.html",{"instructor":instructor})


# employee
@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

@employee_required
def employee_add(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employees/employee_add.html', {'form': form})

@employee_required
def employee_edit(request, pk):
    employee = Employee.objects.filter(pk=pk).first()
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employees/employee_edit.html', {'form': form})

@employee_required
def employee_delete(request, pk):
    employee = Employee.objects.filter(pk=pk).first()
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_delete.html', {'employee': employee})

# user
@employee_required
def user_list(request):
    users = User.objects.all().select_related(
            'student', 'instructor', 'employee'
        ).order_by('-date_joined')
        
        # Count users by role
    student_count = User.objects.filter(role='student').count()
    instructor_count = User.objects.filter(role='instructor').count()
    employee_count = User.objects.filter(role='employee').count()
    total_users = users.count()
    context = {
            'users': users,
            'total_users': total_users,
            'student_count': student_count,
            'instructor_count': instructor_count,
            'employee_count': employee_count,
        }     
    return render(request, 'users/user_list.html', context)
    
def home_redirect(request):
    return redirect('/login/')

# Authentication Views
@employee_required
def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        role = request.POST.get('role')
        
        if user_form.is_valid():
            # Create user with hashed password
            user = user_form.save(commit=False)
            user.password = make_password(user_form.cleaned_data['password1'])
            user.save()
            
            # Create profile based on role with additional data
            if role == 'student':
                Student.objects.create(user=user, name=user.username)
                messages.success(request, f'Student account created for {user.username}! Please login.')
                
            elif role == 'instructor':
                Instructor.objects.create(user=user, name=user.username)
                messages.success(request, f'Instructor account created for {user.username}! Please login.')
                
            elif role == 'employee':
                Employee.objects.create(user=user, name=user.username)
                messages.success(request, f'Employee account created for {user.username}! Please login.')
            
            return redirect('/login/')
        else:
            messages.error(request, 'Please correct the errors below.')
    
    else:
        user_form = RegisterForm()
    
    return render(request, 'users/register.html', {'user_form': user_form})

@unauthenticated_user
def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                # Set session variables
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                request.session['role'] = user.role
                
                messages.success(request, f'Welcome back, {user.username}!')
                
                # USE ONLY DIRECT PATHS - NO REVERSE NAMES
                return redirect('/dashboard/')
                
            else:
                messages.error(request, "Incorrect password")
        except User.DoesNotExist:
            messages.error(request, "User not found")

    return render(request, 'users/login.html')

def custom_logout(request):
    request.session.flush()
    messages.success(request, 'You have been logged out successfully.')
    return redirect('/login/')

# Helper function to get current user
def get_current_user(request):
    if 'user_id' in request.session:
        try:
            return User.objects.get(id=request.session['user_id'])
        except User.DoesNotExist:
            return None
    return None
