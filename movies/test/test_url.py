from django.test import SimpleTestCase
from django.urls import reverse, resolve
from movies.views import search, TagCreate, TagDelete

class TestUrls(SimpleTestCase):

    def test_search_url(self):
        url = reverse('movies-search')
        self.assertEquals(resolve(url).func, search)

    def test_create_tag_url(self):
        url = reverse('tag-create')
        self.assertEquals(resolve(url).func.view_class, TagCreate)

    def test_delete_tag_url(self):
        url = reverse('tag-delete', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, TagDelete)