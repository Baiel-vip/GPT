from django.contrib import admin
from student.models import Course, Teacher, Student
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','course')
    list_display_links = ('id','first_name','last_name')
    search_fields = ('first_name','last_name','email')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','student_number')
    list_display_links = ('id','first_name','last_name')
    list_filter = ('course__name',)
    search_fields = ('first_name','last_name','email')


# Register your models here.
