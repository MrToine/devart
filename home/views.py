from django.shortcuts import render
from courses.models import Course 

def home(request):
    courses = Course.objects.order_by('-created_at')[:6]
    return render(request, 'home.html', {'courses': courses}) 
