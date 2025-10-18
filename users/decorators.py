from django.shortcuts import redirect
from django.contrib import messages

def login_required(view_func):
    """
    Decorator to check if user is logged in via session
    """
    def wrapper_func(request, *args, **kwargs):
        if 'user_id' in request.session:
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, "Please login to access this page.")
            return redirect('/login/')  # DIRECT PATH
    return wrapper_func

def role_required(allowed_roles=[]):
    """
    Decorator for views that checks if the user has the required role.
    """
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if 'user_id' in request.session:
                from .models import User
                try:
                    user = User.objects.get(id=request.session['user_id'])
                    if user.role in allowed_roles:
                        return view_func(request, *args, **kwargs)
                    else:
                        messages.error(request, "You don't have permission to access this page.")
                        # REDIRECT USING DIRECT PATHS ONLY
                        return redirect('/dashboard/')
                except User.DoesNotExist:
                    messages.error(request, "User not found.")
                    return redirect('/login/')
            else:
                messages.error(request, "Please login to access this page.")
                return redirect('/login/')
        return wrapper_func
    return decorator

def admin_required(view_func):
    """
    Decorator for views that require admin/staff access
    """
    def wrapper_func(request, *args, **kwargs):
        if 'user_id' in request.session:
            from .models import User
            try:
                user = User.objects.get(id=request.session['user_id'])
                if user.is_staff or user.is_superuser:
                    return view_func(request, *args, **kwargs)
                else:
                    messages.error(request, "Admin access required.")
                    return redirect('/login/')
            except User.DoesNotExist:
                messages.error(request, "User not found.")
                return redirect('/login/')
        else:
            messages.error(request, "Please login to access this page.")
            return redirect('/login/')
    return wrapper_func

# Specific role decorators - SIMPLIFIED
def student_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'user_id' in request.session:
            from .models import User
            try:
                user = User.objects.get(id=request.session['user_id'])
                if user.role == 'student':
                    return view_func(request, *args, **kwargs)
                else:
                    messages.error(request, "Student access required.")
                    return redirect('/dashboard/')
            except User.DoesNotExist:
                return redirect('/login/')
        else:
            return redirect('/login/')
    return wrapper

def instructor_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'user_id' in request.session:
            from .models import User
            try:
                user = User.objects.get(id=request.session['user_id'])
                if user.role == 'instructor':
                    return view_func(request, *args, **kwargs)
                else:
                    messages.error(request, "Instructor access required.")
                    return redirect('/dashboard/')
            except User.DoesNotExist:
                return redirect('/login/')
        else:
            return redirect('/login/')
    return wrapper

def employee_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'user_id' in request.session:
            from .models import User
            try:
                user = User.objects.get(id=request.session['user_id'])
                if user.role == 'employee':
                    return view_func(request, *args, **kwargs)
                else:
                    messages.error(request, "Employee access required.")
                    return redirect('/dashboard/')
            except User.DoesNotExist:
                return redirect('/login/')
        else:
            return redirect('/login/')
    return wrapper

def unauthenticated_user(view_func):
    """
    Redirect to dashboard if user is already authenticated
    """
    def wrapper_func(request, *args, **kwargs):
        if 'user_id' in request.session:
            return redirect('/dashboard/')  # DIRECT PATH
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func