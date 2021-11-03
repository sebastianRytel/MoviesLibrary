from django import forms
from django.forms import ModelForm

from movies.models import Movies, MovieTag


class MoviesForm(ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'
        widgets = {
            'Rating': forms.RadioSelect(),
            'Location': forms.RadioSelect(),
        }


    movie_tag = forms.ModelMultipleChoiceField(
        queryset=MovieTag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

class MovieTagForm(ModelForm):
    class Meta:
        model = MovieTag
        fields = '__all__'
