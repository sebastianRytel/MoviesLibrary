import ast

from movies.db.models import Movies

def create_data(data_from_search):
    dict_with_movie_details = {}
    for key, value in ast.literal_eval(data_from_search).items():
        if hasattr(Movies, key):
            dict_with_movie_details[key] = value
    return dict_with_movie_details