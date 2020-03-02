from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Article(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    text = models.TextField(db_index=True)
    slug = models.SlugField(max_length=300, unique_for_date='created_date')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article_author')
    startup = models.ForeignKey('Startup', on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tag', blank=True, related_name='articles')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    edited_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog:article_details', kwargs={'pk': self.pk})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Startup(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
