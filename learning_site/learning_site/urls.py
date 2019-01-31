from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('courses/', include('courses.urls')),
    path('admin/', admin.site.urls),
    path(r'', views.hello_world)
]
