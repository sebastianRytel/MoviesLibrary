from movies.db.models import Movies
from django_filters import ChoiceFilter, MultipleChoiceFilter, FilterSet

class MovieFilter(FilterSet):

    RANKING_CHOICES = (
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
        (0, '0'),
    )

    WHERE_TO_WATCH = (
        ('HARD DRIVE', 'harddrive'),
        ('CDA', 'cda'),
        ('NETFLIX', 'Netflix')
    )

    Location = ChoiceFilter(choices=WHERE_TO_WATCH, empty_label='All')
    Rating = MultipleChoiceFilter(choices=RANKING_CHOICES)

    class Meta:
        model = Movies
        fields = {
            'Title': ['icontains'],
            'Year': ['exact'],
            'movie_tag': ['exact'],
            'Rating': ['exact'],
            'watched': ['exact'],
        }
