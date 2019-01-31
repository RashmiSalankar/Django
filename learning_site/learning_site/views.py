#from django.http import HttpResponse

#def hello_world(request):
#    return HttpResponse("Hello World!")

from django.shortcuts import render

def hello_world(request):
    return render(request, 'home.html')