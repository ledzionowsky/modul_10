import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular?api_key=f126183eb3be2f0572109b4f17dd9260"
    response = requests.get(endpoint)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=f126183eb3be2f0572109b4f17dd9260"
    response = requests.get(endpoint)
    return response.json()

def get_movies_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images/credits?api_key=f126183eb3be2f0572109b4f17dd9260"
    response = requests.get(endpoint)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=f126183eb3be2f0572109b4f17dd9260"
    response = requests.get(endpoint)
    return response.json()["cast"]

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}?api_key=f126183eb3be2f0572109b4f17dd9260"
    response = requests.get(endpoint)
    response.raise_for_status()
    return response.json()

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]
