from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from movies.services.create_data_for_db import create_data
from movies.services.searcher import search_all, search_exact, search_by_id
from movies.services.new_tag_from_search import create_new_tag
from movies.db.form import MoviesForm, MovieTagForm, LocationForm, UserCommitForm
from movies.db.models import Movies, MovieTag, MovieLocation
from movies.db.filters import MovieFilter


def home(request):
    return render(request, 'movies/home.html')

def search(request):
    if request.method == "POST":
        movie_title_all = request.POST.get('search_all')
        movie_title_exact = request.POST.get('search_exact')
        movie_id = request.POST.get('search_by_id')
        if movie_title_all:
            return render(request, 'movies/movie/search.html', {'movies': search_all(movie_title_all)})
        elif movie_title_exact:
            return render(request, 'movies/movie/search.html', {'movies': search_exact(movie_title_exact)})
        elif movie_id:
            return render(request, 'movies/movie/search.html', {'movies': [search_by_id(movie_id)]})
    return render(request, 'movies/movie/search.html')


def save_to_library(request):
    if request.method == 'POST':
        movies = MoviesForm(request.POST)
        movie_locations = LocationForm(request.POST)
        context = {
            'movies_form': movies,

            'movie_locations_form': movie_locations,
        }
        if movies.is_valid() and movie_locations.is_valid():
            new_tags = create_new_tag(movies.cleaned_data)
            movie_title = movies.cleaned_data['Title']
            movie_locations = MovieLocation.objects.create(**movie_locations.cleaned_data)
            movie_locations.save()
            movie = Movies.objects.create(**movies.cleaned_data, movie_location=movie_locations)
            movie.save()
            return render(request, 'movies/movie/saved_to_db.html', {'title': movie_title, 'new_tags': new_tags})
        # returns form with validation errors, if fields are not valid as per fields definition in models.
        return render(request, 'movies/forms/form.html', context)


class MovieCreateEmpty(CreateView):
    form_class = MoviesForm
    model = Movies
    template_name = 'movies/forms/form_empty.html'

    def get(self, *args, **kwargs):
        resp = super().get(*args, **kwargs)
        return resp


class MovieCreate(CreateView):
    form_class = MoviesForm
    model = Movies
    template_name = 'movies/forms/form.html'

    def post(self, request, *args, **kwargs):
        movie_details = request.POST.get('open movie details')
        processed_data = create_data(movie_details)
        context = {
            'movies_form': MoviesForm(initial=processed_data),
            'movie_locations_form': LocationForm(),
        }
        return render(request, 'movies/forms/form.html', context)


class LibraryView(ListView):
    model = Movies
    template_name = 'movies/movie/library.html'
    context_object_name = 'movies'
    ordering = ['Title', 'Year']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MovieFilter(self.request.GET, queryset=self.get_queryset())
        return context


class MovieDetailView(DetailView):
    model = Movies
    template_name = 'movies/movie/movies_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context['location'] = MovieLocation.objects.all()
        return context

class MovieUpdate(LoginRequiredMixin, UpdateView):
    form_class = MoviesForm
    model = Movies
    context_object_name = 'movie'
    template_name = 'movies/forms/form_update.html'


class MovieDelete(DeleteView):
    model = Movies
    template_name = "movies/movie/movie_delete.html"
    success_url = reverse_lazy("movies-library")


class TagCreate(LoginRequiredMixin, CreateView):
    form_class = MovieTagForm
    model = MovieTag
    template_name = 'movies/tag/tag_create.html'
    extra_context = {"update": False}


class TagList(ListView):
    model = MovieTag
    context_object_name = 'tags'
    ordering = ['tag']
    template_name = 'movies/tag/tags_list.html'


class TagUpdate(UpdateView):
    form_class = MovieTagForm
    model = MovieTag
    context_object_name = 'tag'
    template_name = 'movies/tag/tag_create.html'
    extra_context = {"update": True}


class TagDelete(DeleteView):
    model = MovieTag
    template_name = "movies/tag/tag_delete.html"
    success_url = reverse_lazy("tags-list")
