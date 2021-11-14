from django.db import models
from django.db.models import TextField
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe


class MovieTag(models.Model):
    tag = models.CharField(max_length=100)
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


class MovieLocation(models.Model):
    CDA = models.CharField(max_length=50, blank=True)
    Netflix = models.CharField(max_length=50, blank=True)
    HboGO = models.CharField(max_length=50, blank=True)
    AmazonPrime = models.CharField(max_length=50, blank=True)
    HardDrive = models.CharField(max_length=50, blank=True)


class Movies(models.Model):

    # RANKING_CHOICES = (
    #     (5, mark_safe('<img src="/media/rating_icos/rating_5_ico.jpg">')),
    #     (4, mark_safe('<img src="/media/rating_icos/rating_4_ico.jpg">')),
    #     (3, mark_safe('<img src="/media/rating_icos/rating_3_ico.jpg">')),
    #     (2, mark_safe('<img src="/media/rating_icos/rating_2_ico.jpg">')),
    #     (1, mark_safe('<img src="/media/rating_icos/rating_1_ico.jpg">')),
    #     (0, mark_safe('<img src="/media/rating_icos/rating_0_ico.jpg">')),
    # )

    RANKING_CHOICES = (
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
        (0, '0'),
    )


    # WHERE_TO_WATCH = (
    #     ('HARD DRIVE', mark_safe('<img src="/media/local_icos/hdd_ico.jpg">')),
    #     ('CDA', mark_safe('<img src="/media/local_icos/cda_ico.jpg">')),
    #     ('NETFLIX', mark_safe('<img src="/media/local_icos/flix_ico.jpg">'))
    # )

    WHERE_TO_WATCH = (
        ('HARD DRIVE', 'HARD DRIVE'),
        ('CDA', 'CDA'),
        ('NETFLIX', 'NETFLIX')
    )

    Title = models.CharField(max_length=100)
    Year = models.IntegerField()
    Runtime = models.CharField(max_length=30, blank=True)
    Genre = models.CharField(max_length=30, blank=True)
    Director = models.CharField(max_length=30, blank=True)
    Actors = models.CharField(max_length=60, blank=True)
    Plot = models.TextField(max_length=300, blank=True)
    user_comments = models.TextField(max_length=200, blank=True)
    Awards = models.CharField(max_length=250, blank=True)
    Poster = models.URLField(max_length=250, blank=True)
    imdbRating = models.CharField(max_length=4, blank=True)
    Metascore = models.CharField(max_length=4, blank=True)
    imdbID = models.CharField(max_length=10, blank=True)
    slug = models.SlugField(max_length=50, blank=True)
    movieURL = models.URLField(max_length=40, blank=True)
    movie_tag = models.ManyToManyField(MovieTag)
    Rating = models.IntegerField(choices=RANKING_CHOICES, default=0)
    Location = models.CharField(max_length=10, choices=WHERE_TO_WATCH, default='')
    watched = models.BooleanField(default=True)
    movie_location = models.ForeignKey(MovieLocation, on_delete=models.PROTECT, verbose_name='movie location')

    class Meta:
        unique_together = ("Title", "Year")

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

    def get_delete_url(self):
        return reverse(
            "movie-delete", kwargs={"slug": self.slug}
        )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.Title+str(self.Year))
        super(Movies, self).save(*args, **kwargs)

