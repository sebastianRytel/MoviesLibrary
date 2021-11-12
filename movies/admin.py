from django.contrib import admin
from movies.db.models import Movies, MovieTag, MovieLocation

admin.site.register(Movies)
admin.site.register(MovieTag)
admin.site.register(MovieLocation)