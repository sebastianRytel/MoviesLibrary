from django.contrib import admin
from movies.models import Movies, MovieTag

admin.site.register(Movies)
admin.site.register(MovieTag)