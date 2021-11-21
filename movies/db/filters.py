from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django_filters import FilterSet, ChoiceFilter, ModelMultipleChoiceFilter

from movies.db.models import Movies, MovieTag


class MovieFilter(FilterSet):
    RANKING_CHOICES = (
        (5, mark_safe(f'<img src="{settings.STATIC_URL}rating_icos/rating_5_ico.jpg">')),
        (4, mark_safe(f'<img src="{settings.STATIC_URL}rating_icos/rating_4_ico.jpg">')),
        (3, mark_safe(f'<img src="{settings.STATIC_URL}rating_icos/rating_3_ico.jpg">')),
        (2, mark_safe(f'<img src="{settings.STATIC_URL}rating_icos/rating_2_ico.jpg">')),
        (1, mark_safe(f'<img src="{settings.STATIC_URL}rating_icos/rating_1_ico.jpg">')),
        (0, mark_safe(f'<img src="{settings.STATIC_URL}rating_icos/rating_0_ico.jpg">')),
    )

    IF_WATCHED = (
        (0, "NO"),
        (1, "YES"),
    )

    Rating = ChoiceFilter(choices=RANKING_CHOICES, widget=forms.RadioSelect)

    watched = ChoiceFilter(choices=IF_WATCHED, widget=forms.RadioSelect, label="Did you see this movie?")

    movie_tag = ModelMultipleChoiceFilter(widget=forms.CheckboxSelectMultiple, queryset=MovieTag.objects.all())

    class Meta:
        model = Movies
        fields = ['Title', 'Rating', 'watched', 'movie_tag']
        filter_vertical = 'watched'
