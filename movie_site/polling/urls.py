from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    url(r'movies/', views.movie_list_view),
    url(r'random_movie/', views.random_movie_view),
    url(r'movies_form/', views.movie_view),
    # url(r'', views.hello_view),
]