from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from movies.searcher import search_all, search_exact, search_by_id
from movies.form import MoviesForm, MovieTagForm
from movies.create_data_for_db import create_data
from movies.models import Movies, MovieTag
from movies.filters import MovieFilter

def home(request):
    return render(request, 'movies/home.html')


def about(request):
    return render(request, 'movies/about.html', {'title': 'About'})


def search(request):
    if request.method == "POST":
        movie_title_all = request.POST.get('search_all')
        movie_title_exact = request.POST.get('search_exact')
        movie_id = request.POST.get('search_by_id')
        if movie_title_all:
            return render(request, 'movies/search.html', {'movies': search_all(movie_title_all)})
        elif movie_title_exact:
            return render(request, 'movies/search.html', {'movies': search_exact(movie_title_exact)})
        elif movie_id:
            return render(request, 'movies/search_id.html', {'movie': search_by_id(movie_id)})
    return render(request, 'movies/search.html')


def save_to_library(request):
    if request.method == 'POST':
        movies = MoviesForm(request.POST)
        if movies.is_valid():
            movies.save()
            return render(request, 'movies/saved_to_db.html')
        # returns form with validation errors, if fields are not valid as per fields definition in models.
        return render(request, 'movies/form.html', {'form': movies})


class MovieCreateEmpty(CreateView):
    form_class = MoviesForm
    model = Movies
    template_name = 'movies/form_empty.html'

    def get(self, *args, **kwargs):
        resp = super().get(*args, **kwargs)
        return resp

class MovieCreate(CreateView):
    form_class = MoviesForm
    model = Movies
    template_name = 'movies/form.html'

    def post(self, request, *args, **kwargs):
        movie_details = request.POST.get('open movie details')
        processed_data = create_data(movie_details)
        movies = MoviesForm(initial=processed_data)
        return render(request, 'movies/form.html', {'form': movies})


class LibraryView(ListView):
    model = Movies
    template_name = 'movies/library.html'
    context_object_name = 'movies'
    ordering = ['Title', 'Year']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MovieFilter(self.request.GET, queryset=self.get_queryset())
        return context

class MovieDetailView(DetailView):
    model = Movies


class MovieUpdate(LoginRequiredMixin, UpdateView):
    form_class = MoviesForm
    model = Movies
    context_object_name = 'movie'
    template_name = 'movies/form_update.html'


class TagCreate(LoginRequiredMixin, CreateView):
    form_class = MovieTagForm
    model = MovieTag
    template_name = 'movies/tag/tag_create.html'
    extra_context = {"update": False}


class TagList(ListView):
    queryset = MovieTag.objects.all()
    context_object_name = 'tags'
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
