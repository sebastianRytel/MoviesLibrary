from django.urls import path

from movies import views
from movies.views import (LibraryView,
                          MovieDetailView,
                          MovieCreate,
                          MovieUpdate,
                          MovieDelete,
                          MovieCreateEmpty,
                          TagCreate,
                          TagUpdate,
                          TagList,
                          TagDelete,
                          )

urlpatterns = [
    path('', views.home, name='movies-home'),
    path('search/', views.search, name='movies-search'),
    path('form_predefined/', MovieCreate.as_view(), name='movies-form'),
    path('form_empty/', MovieCreateEmpty.as_view(), name='movie-form-empty'),
    path('save_to_library/', views.save_to_library, name='movies-save'),
    path('library/', LibraryView.as_view(), name='movies-library'),
    path('library/<str:slug>/update', MovieUpdate.as_view(), name='movie-update'),
    path('library/<str:slug>/detail', MovieDetailView.as_view(), name='movie-detail'),
    path('library/<str:slug>/delete', MovieDelete.as_view(), name='movie-delete'),
    path('tag/', TagList.as_view(), name='tags-list'),
    path('tag/create', TagCreate.as_view(), name='tag-create'),
    path("tag/<str:slug>/delete/", TagDelete.as_view(), name="tag-delete"),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag-update'),
]
