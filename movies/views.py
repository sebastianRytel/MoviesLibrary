from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import transaction

from movies.services.create_data_for_db import create_data
from movies.services.searcher import search_all, search_exact, search_by_id
from movies.services.new_tag_from_search import create_new_tag
from movies.db.form import MoviesForm, MovieTagForm, LocationForm, UserCommitForm, MoviesFormSet
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


class MovieCreateEmpty(LoginRequiredMixin, CreateView):
    form_class = MoviesForm
    model = Movies
    # template_name = 'movies/forms/form_empty.html'

    def get(self, request, *args, **kwargs):
        context = {
            'movies_form': MoviesForm(),
            'movie_locations_form': LocationForm(),
        }
        return render(request, 'movies/forms/form_empty.html', context)


class MovieCreate(LoginRequiredMixin, CreateView):
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

class LibraryView(LoginRequiredMixin, ListView):
    model = Movies
    template_name = 'movies/movie/library.html'
    context_object_name = 'movies'
    ordering = ['Title', 'Year']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MovieFilter(self.request.GET, queryset=self.get_queryset())
        return context

class MovieDetailView(LoginRequiredMixin, DetailView):
    model = Movies
    template_name = 'movies/movie/movies_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        movie = self.get_object()
        context['location'] = MovieLocation.objects.filter(id=movie.movie_location_id)
        return context


class MovieUpdate(LoginRequiredMixin, UpdateView):
    form_class = MoviesForm
    model = Movies
    template_name = 'movies/forms/form_update.html'

    def get_context_data(self, **kwargs):
        data = super(MovieUpdate, self).get_context_data(**kwargs)
        data['movie'] = MoviesFormSet(instance=self.object)
        print(data)
        return data

    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     titles = context['titles']
    #     with transaction.atomic():
    #         form.instance.created_by = self.request.user
    #         self.object = form.save()
    #         if titles.is_valid():
    #             titles.instance = self.object
    #             titles.save()
    #     return super(MovieUpdate, self).form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     movie = self.get_object()
    #     context['second_model'] = MovieLocation.objects.get(id=movie.movie_location_id)
    #
    #     context['form'] = self.form_class(instance=self.object)
    #     context['form2'] = self.second_form_class(initial={
    #         'CDA': self.object.movie_location.CDA,
    #         'Netflix': self.object.movie_location.Netflix,
    #         'HboGO': self.object.movie_location.HboGO,
    #         'AmazonPrime': self.object.movie_location.AmazonPrime,
    #         'HardDrive': self.object.movie_location.HardDrive,
    #     })
    #     return context
    #



class MovieDelete(LoginRequiredMixin, DeleteView):
    model = Movies
    template_name = "movies/movie/movie_delete.html"
    success_url = reverse_lazy("movies-library")


class TagCreate(LoginRequiredMixin, CreateView):
    form_class = MovieTagForm
    model = MovieTag
    template_name = 'movies/tag/tag_create.html'
    extra_context = {"update": False}


class TagList(LoginRequiredMixin, ListView):
    model = MovieTag
    context_object_name = 'tags'
    ordering = ['tag']
    template_name = 'movies/tag/tags_list.html'


class TagUpdate(LoginRequiredMixin, UpdateView):
    form_class = MovieTagForm
    model = MovieTag
    context_object_name = 'tag'
    template_name = 'movies/tag/tag_create.html'
    extra_context = {"update": True}


class TagDelete(LoginRequiredMixin, DeleteView):
    model = MovieTag
    template_name = "movies/tag/tag_delete.html"
    success_url = reverse_lazy("tags-list")
