from crispy_forms.layout import Row, Column, Div, ButtonHolder, Submit
from crispy_forms.helper import FormHelper, Layout
from django import forms
from django.forms import ModelForm


from movies.db.models import Movies, MovieTag, MovieLocation


class MoviesForm(ModelForm):
    class Meta:
        model = Movies
        fields = ['Title', 'Year', 'Runtime', 'Genre', 'Director', 'Actors', 'Plot', 'Awards', 'Poster',
                  'imdbRating', 'Metascore', 'imdbID', 'movieURL']


class UserCommitForm(ModelForm):
    class Meta:
        model = Movies
        fields = ['Rating', 'movie_tag', 'Location', 'watched', 'user_comments']

    movie_tag = forms.ModelMultipleChoiceField(
        queryset=MovieTag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class LocationForm(ModelForm):
    class Meta:
        model = MovieLocation
        fields = '__all__'
        exclude = ['location_dict']

class MovieTagForm(ModelForm):
    class Meta:
        model = MovieTag
        fields = '__all__'

