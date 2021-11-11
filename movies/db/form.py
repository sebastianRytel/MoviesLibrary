from crispy_forms.layout import Row, Column, Div, ButtonHolder, Submit
from crispy_forms.helper import FormHelper, Layout
from django import forms
from django.forms import ModelForm


from movies.db.models import Movies, MovieTag


class MoviesForm(ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'
        widgets = {
            'Rating': forms.RadioSelect(),
            'Location': forms.RadioSelect(),
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
                        Column('user_comments', css_class='form-group col-md-12 mb-0'),
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
                    ), css_class='form-group col-md-8 mb-0 column-left'),
                Column(
                    Column('Rating', css_class='column-right-row'),
                    Column('movie_tag', css_class='column-right-row'),
                    Column('Location', css_class='column-right-row'),
                    Column('watched', css_class='column-right-row'),
                css_class='form-group col-md-4 mb-0 column-right'),
                ),

            ButtonHolder(
                Submit('Save in Library', 'Save', css_class='btn btn-danger'),
                ),
        )

class MovieTagForm(ModelForm):
    class Meta:
        model = MovieTag
        fields = '__all__'
