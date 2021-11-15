from django.contrib import admin
from movies.db.models import Movies, MovieTag

admin.site.register(Movies)
admin.site.register(MovieTag)
