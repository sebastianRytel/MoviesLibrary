import ast

import requests

url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "b5d9716ba4msh6da311e3a53c32bp1ed818jsn7a57ebf9abc6"
}


def search_for_movie_by_title(movie_title):
    list_of_searched_movies = []
    querystring = {"s": f"{movie_title}", "r": "json", "page": "1"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    response_to_dict = ast.literal_eval(response.text)
    if response_to_dict["Response"] == "False":
        return response_to_dict
    for element in response_to_dict["Search"]:
        movie_id = search_by_id(element.get('imdbID'))
        list_of_searched_movies.append(movie_id)
    return list_of_searched_movies


def search_by_id(movie_id):
    querystring = {"r": "json", "i": f"{movie_id}"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    response_to_dict = ast.literal_eval(response.text)
    response_to_dict['movieURL'] = f"https://www.imdb.com/title/{response_to_dict['imdbID']}"
    return response_to_dict


def search_all(movie_title):
    return search_for_movie_by_title(movie_title)


def search_exact(movie_title):
    searched_movies_all = search_for_movie_by_title(movie_title)
    return [movie for movie in searched_movies_all if movie['Title'] == movie_title]
