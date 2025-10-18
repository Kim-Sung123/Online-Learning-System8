from django.urls import path
from .import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_add, name='category_add'),
    path('categories/edit/<int:pk>/', views.category_edit, name='category_edit'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),
    
    path('tags/', views.tag_list, name='tag_list'),
    path('tags/add/', views.tag_add, name='tag_add'),
    path('tags/edit/<int:pk>/', views.tag_edit, name='tag_edit'),
    path('tags/delete/<int:pk>/', views.tag_delete, name='tag_delete'),

    path("courses/",views.course_list,name="course_list"),
    path("courses/add/",views.course_add,name="course_add"),
    path("courses/edit/<int:pk>/",views.course_edit,name="course_edit"),
    path("courses/delete/<int:pk>/",views.course_delete,name="course_delete"),
    
    # enrollment
    path("enrollments/",views.enrollment_list,name="enrollment_list"),
    path("enrollments/add/",views.enrollment_add,name="enrollment_add"),
    path("enrollments/edit/<int:pk>/",views.enrollment_edit,name="enrollment_edit"),
    path("enrollments/delete/<int:pk>/",views.enrollment_delete,name="enrollment_delete"),
    
    # lesson
    path("lessons/",views.lesson_list,name="lesson_list"),
    path("lessons/add/",views.lesson_add,name="lesson_add"),
    path("lessons/edit/<int:pk>/",views.lesson_edit,name="lesson_edit"),
    path("lessons/delete/<int:pk>/",views.lesson_delete,name="lesson_delete"),
]
