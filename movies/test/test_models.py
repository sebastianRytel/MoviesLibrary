from django.test import TestCase
from movies.db.models import MovieTag


class TestModels(TestCase):

    def setUp(self):
        self.movie_tag_1 = MovieTag.objects.create(
            tag='horror',
            slug='horror',
        )

    def test_tag_creation(self):
        self.assertEquals(self.movie_tag_1.tag, 'horror')