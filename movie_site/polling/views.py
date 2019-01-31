from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm
from django.db.models.aggregates import Count
from random import randint

# Create your views here.
def hello_view(request):
    return HttpResponse("Hello World!")

def movie_list_view(request):
    movies = Movie.objects.all()
    return render(request, 'movie_poll.html', {'movies': movies})

def random_movie_view(request):
    movies = Movie.objects.all()
    random_movie = Movie.random(movies)
    return HttpResponse(random_movie)

def movie_view(request):
    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "movies/movie_save.html", context)


