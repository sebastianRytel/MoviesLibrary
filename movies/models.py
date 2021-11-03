from django.db import models
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.template.defaultfilters import slugify

class MovieTag(models.Model):
    tag = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(
        help_text="A label for URL config.",
        max_length=31,
        populate_from=["tag"],
    )

    class Meta:
        ordering = ['tag']

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse(
            "tags-list",
        )


    def get_update_url(self):
        return reverse(
            "tag-update", kwargs={"slug": self.slug}
        )


    def get_delete_url(self):
        return reverse(
            "tag-delete", kwargs={"slug": self.slug}
        )


class Movies(models.Model):

    class Rank(models.IntegerChoices):
        VERY_GOOD = 5,
        GOOD = 4,
        AVERAGE = 3,
        POOR = 2,
        BAD = 1,
        PIECE_OF_SHIT = 0,

    WhereToWatch = models.TextChoices('WhereToWatch', 'Harddrive CDA Netflix')

    Title = models.CharField(max_length=100)
    Year = models.IntegerField()
    Runtime = models.CharField(max_length=30, blank=True)
    Genre = models.CharField(max_length=30, blank=True)
    Director = models.CharField(max_length=30, blank=True)
    Actors = models.CharField(max_length=60, blank=True)
    Plot = models.TextField(max_length=250, blank=True)
    Awards = models.CharField(max_length=250, blank=True)
    Poster = models.URLField(max_length=250, blank=True)
    imdbRating = models.CharField(max_length=4, blank=True)
    Metascore = models.CharField(max_length=4, blank=True)
    imdbID = models.CharField(max_length=10, blank=True)
    Rating = models.IntegerField(choices=Rank.choices, default='')
    Location = models.CharField(max_length=10,choices=WhereToWatch.choices, default='')
    movieURL = models.URLField(max_length=40, blank=True)
    movie_tag = models.ManyToManyField(MovieTag)
    slug = models.SlugField(max_length=50, blank=True)

    class Meta:
        unique_together = ("Title", "Year", "slug")

    def __str__(self):
        return f'{self.Title}'

    def get_absolute_url(self):
        return reverse(
            "movie-detail", kwargs={"slug": self.slug}
        )

    def get_update_url(self):
        return reverse(
            "movie-update", kwargs={"slug": self.slug}
        )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.Title+str(self.Year))
        super(Movies, self).save(*args, **kwargs)
