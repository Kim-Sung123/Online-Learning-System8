from django.shortcuts import render, redirect
from users.decorators import login_required, student_required, instructor_required, employee_required
from users.models import Student, Instructor, Employee, User
from course_management.models import Course,Lessons,Enrollments,Category,Tag

# Helper function to get current user
def get_current_user(request):
    if 'user_id' in request.session:
        try:
            return User.objects.get(id=request.session['user_id'])
        except User.DoesNotExist:
            return None
    return None

@login_required
def home(request):
    """Main dashboard that redirects based on role"""
    try:
        user = User.objects.get(id=request.session['user_id'])
        if user.role == 'student':
            return redirect('/dashboard/student/')
        elif user.role == 'instructor':
            return redirect('/dashboard/instructor/')
        elif user.role == 'employee':
            return redirect('/dashboard/employee/')
        else:
            # FIX: Use 'dashboard/home.html' instead of 'dashboards/home.html'
            return render(request, 'dashboard/home.html', {'user': user})
    except User.DoesNotExist:
        return redirect('/login/')

@student_required
def student_dashboard(request):
    """Student Dashboard"""
    user = get_current_user(request)
    student = Student.objects.get(user=user)
    total_enrollment = Enrollments.objects.count()
    context = {
        'student': student,
        'total_enrollment' : total_enrollment,
        'enrolled_courses': [
            {'name': 'Python Programming', 'progress': 75, 'next_assignment': 'Final Project', 'due_date': '2025-10-20'},
            {'name': 'Web Development', 'progress': 45, 'next_assignment': 'CSS Styling', 'due_date': '2025-10-15'},
        ],
        'upcoming_assignments': [
            {'course': 'Python Programming', 'assignment': 'Final Project', 'due_date': '2025-10-20', 'days_left': 9},
        ]
    }
    return render(request, 'dashboard/student_dashboard.html', context)

@instructor_required
def instructor_dashboard(request):
    """Instructor Dashboard"""
    user = get_current_user(request)
    instructor = Instructor.objects.get(user=user)
    total_students = Student.objects.count()
    total_course = Course.objects.count()
    context = {
        'instructor': instructor,
        'total_students': total_students,
        'total_courses': total_course,
        'own_courses': [
            {'name': 'Advanced Python', 'students': 45, 'rating': 4.7, 'revenue': '$2,250'},
            {'name': 'Machine Learning', 'students': 32, 'rating': 4.8, 'revenue': '$1,920'},
        ]
    }
    # FIX: Use 'dashboard/instructor_dashboard.html' instead of 'dashboards/instructor_dashboard.html'
    return render(request, 'dashboard/instructor_dashboard.html', context)

@employee_required
def employee_dashboard(request):
    """Employee Dashboard"""
    user = get_current_user(request)
    employee = Employee.objects.get(user=user)
    total_course = Course.objects.count()
    # Get real statistics
    total_students = Student.objects.count()
    total_instructors = Instructor.objects.count()
    total_employees = Employee.objects.count()
    total_users = User.objects.count()
    
    total_lesson = Lessons.objects.count()
    total_enrollment = Enrollments.objects.count()
    total_category = Category.objects.count()
    total_tags = Tag.objects.count()
    context = {
        'employee': employee,
        'system_stats': {
            'total_users': total_users,
            'total_students': total_students,
            'total_instructors': total_instructors,
            'total_employees': total_employees,
            'total_courses': total_course,
            'total_lesson' : total_lesson, 
            'total_enrollments': total_enrollment,
            'total_category' : total_category,
            'total_tag ' :total_tags,
            'active_users_week': 287,
            'system_uptime': '99.9%'
        },
        'recent_activity': [
            {'type': 'New Student', 'description': 'John Doe registered', 'time': '2 hours ago'},
            {'type': 'Course Enrollment', 'description': 'Python course - 5 new enrollments', 'time': '5 hours ago'},
        ],
        'management_links': [
            {'name': 'User Management', 'url': '/admin/users/user/', 'icon': '👥'},
            {'name': 'Student Management', 'url': '/students/', 'icon': '🎓'},
            {'name': 'Instructor Management', 'url': '/instructors/', 'icon': '👨‍🏫'},
            {'name': 'Employee Management', 'url': '/employees/', 'icon': '💼'},
            {'name': 'Django Admin', 'url': '/admin/', 'icon': '⚙️'},
        ]
    }
    # FIX: Use 'dashboard/employee_dashboard.html' instead of 'dashboards/employee_dashboard.html'
    return render(request, 'dashboard/employee_dashboard.html', context)