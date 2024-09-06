from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name ='list-student'),
    path('create/', views.create_student, name ='create-student'),
    path('students/delete/', views.delete_student, name='delete-student'),

]

