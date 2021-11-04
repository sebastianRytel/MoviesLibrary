import django_filters
from movies.models import Movies

class MovieFilter(django_filters.FilterSet):

    class Meta:
        model = Movies
        fields = {
            'Title': ['icontains'],
            'Year': ['exact'],
            'movie_tag': ['exact'],
            'Rating': ['exact'],
            'watched': ['exact'],
        }