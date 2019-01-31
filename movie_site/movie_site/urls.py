from django.contrib import admin
from django.urls import path, include
from polling.views import movie_list_view #, movie_view

urlpatterns = [
    # path('movies/', movie_list_view),
    path('movies/', include('polling.urls')),
    path('random_movie/', include('polling.urls')),
    path(r'', include('polling.urls')),
    # path('polling/', include('polling.urls')),
    path('admin/', admin.site.urls),    # not admin.movie_site.urls
]