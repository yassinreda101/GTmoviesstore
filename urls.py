from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.movie_list, name='movie_list'),  # Home page showing movies
]
