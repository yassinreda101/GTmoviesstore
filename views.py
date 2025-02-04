import requests
from django.shortcuts import render

TMDB_API_KEY = 'f49ee15982dacdc9d7551d19e7e53358' 
def movie_list(request):
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    movies = response.json().get('results', [])

    return render(request, 'movies/movie_list.html', {'movies': movies})
