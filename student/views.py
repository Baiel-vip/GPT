from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

from student.forms import StudentForm
from student.models import Student


def home(request):
    return render(request, 'student/home.html')


def student_list(request):
        students = Student.objects.all()
        return render(request, 'student/students_list.html', {'students': students})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list-student')

        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # email = request.POST['email']
        # age = request.POST['age']
        # student_number = request.POST['student_number']

        # Student.objects.create(
        #     first_name=first_name,
        #     last_name=last_name,
        #     email=email,
        #     age=age,
        #     student_number=student_number
        # )
        # return redirect('student_list')
    else:
        form = StudentForm()
        return render(request, 'student/create_student.html', {'form': form})

def edit_student(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list-student')
    else:
        form = StudentForm(instance=student)
        return render(request, 'student/create_student.html', {'form': form})

def delete_student(request,pk):
    try:

        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return redirect('list-student')
    student.delete()
    return redirect('list-student')