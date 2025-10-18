from django.urls import path
from . import views


urlpatterns = [
    # students
    path("students/",views.student_list,name="student_list"),
    path("students/add/",views.student_add,name="student_add"),
    path("students/edit/<int:pk>/",views.student_edit,name="student_edit"),
    path("students/delate/<int:pk>/",views.student_delete,name="student_delete"),
    # instructor
    path("instructors/",views.instructor_list,name="instructor_list"),
    path("instructors/add/",views.instructor_add,name="instructor_add"),
    path("instructors/edit/<int:pk>/",views.instructor_edit,name="instructor_edit"),
    path("instructors/delete/<int:pk>/",views.instructor_delete,name="instructor_delete"),
    # employees
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.employee_add, name='employee_add'),
    path('employeesedit/<int:pk>/', views.employee_edit, name='employee_edit'),
    path('employees/delete/<int:pk>/', views.employee_delete, name='employee_delete'),
    
    # users
    path('', views.home_redirect, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('user_list/', views.user_list, name='user_list'),
]