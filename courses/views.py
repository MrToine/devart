from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Course, Lesson

def list(request):
    courses = Course.objects.all()
    return render(request, 'courses/list.html', {'courses': courses})

def show(request, course_name, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.filter(course_id=course_id)
    return render(request, 'courses/show.html', {'course' : course, 'lessons': lessons})