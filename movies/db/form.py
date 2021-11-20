from crispy_forms.layout import Row, Column, Div, ButtonHolder, Submit
from crispy_forms.helper import FormHelper, Layout
from django import forms
from django.forms import ModelForm
from django.utils.safestring import mark_safe

from movies.db.models import Movies, MovieTag


class MoviesForm(ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'
        widgets = {
            'Rating': forms.RadioSelect(),
            'Location': forms.RadioSelect(),
        }
        labels = {
            'CDA': mark_safe('<img src="/staticfiles/media/local_icos/cda_ico.jpg">'),
            'HardDrive': mark_safe('<img src="/staticfiles/media/local_icos/hdd_ico.jpg">'),
            'Netflix': mark_safe('<img src="/staticfiles/media/local_icos/flix_ico.jpg">'),
            'HboGO': mark_safe('<img src="/staticfiles/media/local_icos/hbo_ico.jpg">'),
            'AmazonPrime': mark_safe('<img src="/staticfiles/media/local_icos/prime_ico.jpg">')
        }

        exclude = ['slug']

    movie_tag = forms.ModelMultipleChoiceField(
        queryset=MovieTag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Plot'].widget.attrs['rows'] = 4
        self.fields['user_comments'].widget.attrs['rows'] = 4
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(
                    Div(
                        Column('Title', css_class='form-group col-md-8 mb-0'),
                        Column('Year', css_class='form-group col-md-4 mb-0'),
                        css_class='form-row',
                    ),
                    Div(
                        Column('Director', css_class='form-group col-md-4 mb-0'),
                        Column('Genre', css_class='form-group col-md-4 mb-0'),
                        Column('Runtime', css_class='form-group col-md-4 mb-0'),
                        css_class='form-row'
                    ),
                    Div(
                        Column('Actors', css_class='form-group col-md-12 mb-0'),
                        Column('Plot', css_class='form-group col-md-12 mb-0'),
                        css_class='form-row'
                    ),
                    Div(
                        Column('Awards', css_class='form-group col-md-6 mb-0'),
                        Column('Poster', css_class='form-group col-md-6 mb-0'),
                        css_class='form-row'
                    ),
                    Div(
                        Column('imdbRating', css_class='form-group col-md-4 mb-0'),
                        Column('Metascore', css_class='form-group col-md-4 mb-0'),
                        css_class='form-row'
                    ),
                    Div(
                        Column('imdbID', css_class='form-group col-md-4 mb-0'),
                        Column('movieURL', css_class='form-group col-md-4 mb-0'),
                        css_class='form-row'
                    ), css_class='form-group col-md-5 mb-0 column-1st'),
                Column(Row('movie_tag', css_class='column-right-row'),
                       css_class='form-group col-md-2 mb-0 column-2nd'),
                Column(
                    Row('Rating', css_class='column-right-row'),
                    Row('user_comments', css_class='column-right-row'),
                    Row('watched', css_class='column-right-row'),
                css_class='form-group col-md-3 mb-0 column-3rd'),

                Column('CDA', 'Netflix', 'HboGO', 'AmazonPrime', 'HardDrive',
                    css_class='form-group col-md-2 mb-0 column-4th'),
                ),

            ButtonHolder(
                Submit('Save in Library', 'Save', css_class='btn btn-danger'),
                ),
        )

class MovieTagForm(ModelForm):
    class Meta:
        model = MovieTag
        fields = '__all__'
