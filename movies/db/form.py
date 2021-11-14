from crispy_forms.layout import Row, Column, Div, ButtonHolder, Submit
from crispy_forms.helper import FormHelper, Layout
from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from movies.db.models import Movies, MovieTag, MovieLocation


class MoviesForm(ModelForm):
    class Meta:
        model = Movies
        fields = ['Title', 'Year', 'Runtime', 'Genre', 'Director', 'Actors', 'Plot', 'Awards', 'Poster',
                  'imdbRating', 'Metascore', 'imdbID', 'movieURL']

class LocationForm(ModelForm):
    class Meta:
        model = MovieLocation
        fields = '__all__'


MoviesFormSet = inlineformset_factory(
    MovieLocation,
    Movies,
    form=MoviesForm,
    extra=1,
)


class UserCommitForm(ModelForm):
    class Meta:
        model = Movies
        fields = ['Rating', 'movie_tag', 'Location', 'watched', 'user_comments']

    movie_tag = forms.ModelMultipleChoiceField(
        queryset=MovieTag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class MovieTagForm(ModelForm):
    class Meta:
        model = MovieTag
        fields = '__all__'

