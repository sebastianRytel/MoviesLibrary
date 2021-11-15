from django import forms
from django.forms import ModelForm

from movies.db.models import Movies, MovieTag


class MoviesForm(ModelForm):
    class Meta:
        model = Movies
        fields = ['Title', 'Year', 'Runtime', 'Genre', 'Director', 'Actors', 'Plot', 'Awards', 'Poster',
                  'imdbRating', 'Metascore', 'imdbID', 'movieURL']

class UserCommitForm(ModelForm):
    class Meta:
        model = Movies
        fields = ['Rating', 'movie_tag', 'watched', 'user_comments', 'CDA', 'Netflix', 'HboGO', 'AmazonPrime',
                  'HardDrive']

    movie_tag = forms.ModelMultipleChoiceField(
        queryset=MovieTag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class MovieTagForm(ModelForm):
    class Meta:
        model = MovieTag
        fields = '__all__'

