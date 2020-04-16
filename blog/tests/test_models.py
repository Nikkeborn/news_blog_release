from django.test import TestCase

# Create your tests here.
from django.utils import timezone

from blog.models import Article, Startup
from django.contrib.auth.models import User

class ArticleModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        user = User.objects.create_user(username='test_user', password='123456',)
        startup = Startup.objects.create(title='new_test_startup', slug='new_test_startup',)
        Article.objects.create(title='Test title', text='Test text text text text text text', slug='test_slug', author=user, startup=startup,)

    def test_title_lable(self):
        article = Article.objects.get(title='Test title')
        field_label = article._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')

    def test_startup_title(self):
        article = Article.objects.get(title='Test title')
        expected_startup = article.startup.title
        self.assertEquals(expected_startup,'new_test_startup')

    def test_author_username(self):
        article = Article.objects.get(title='Test title')
        expected_author = article.author.username
        self.assertEquals(expected_author,'test_user')

    def test_slug(self):
        article = Article.objects.get(title='Test title')
        expected_slug = article.slug
        self.assertEquals(expected_slug, 'test_slug')

    def test_get_absolute_url_method(self):
        article = Article.objects.get(title='Test title')
        pk = article.pk
        expected_url = article.get_absolute_url()
        self.assertEquals(expected_url, f'/article/{pk}/details')

    def test_published_date(self):
        article = Article.objects.get(title='Test title')
        expected_published_date = article.published_date.date()
        self.assertEquals(expected_published_date, timezone.localdate())
