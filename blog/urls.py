from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('articles/search', Search.as_view(), name='search'),
    path('articles/', ArticleList.as_view(), name='articles'),
    path('tags/', TagList.as_view(), name='tags'),
    path('startups/', StartupList.as_view(), name='startups'),
    path('article/<int:pk>/details', ArticleDetails.as_view(), name='article_details'),
    path('article/<int:pk>/edit', ArticleEdit.as_view(), name='article_edit'),
    path('article/<int:pk>/delete', ArticleDelete.as_view(), name='article_delete'),
    path('tag/<int:pk>/delete', TagDelete.as_view(), name='tag_delete'),
    path('startup/<int:pk>/delete', StartupDelete.as_view(), name='startup_delete'),
    path('author/<int:pk>/', AuthorDetails.as_view(), name='author_details'),
    path('new/article/', NewArticle.as_view(), name='new_article'),
    path('new/tag/', NewTag.as_view(), name='new_tag'),
    path('new/startup/', NewStartup.as_view(), name='new_startup'),
]