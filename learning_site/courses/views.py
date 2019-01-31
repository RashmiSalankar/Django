from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

# Create your views here.
def course_list2(request):
    courses = Course.objects.all()
    output = ', '.join([str(course) for course in courses])
    return HttpResponse(output)

def course_list1(request):
    courses = Course.objects.all()
    output = "There are " + str(courses.count()) + " courses"
    #return HttpResponse("There are {0} courses", courses.count())
    return HttpResponse(output)

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})
