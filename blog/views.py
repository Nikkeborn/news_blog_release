from django.views.generic import ListView, View, DeleteView, UpdateView, CreateView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from .utils import *
from .forms import *


class TagList(ListView):
    template_name = 'blog/tags.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return Tag.objects.all()


class StartupList(ListView):
    model = Startup
    template_name = 'blog/startups.html'
    context_object_name = 'startups'


class ArticleList(ListView):
    model = Article
    template_name = 'blog/articles.html'
    context_object_name = 'articles'


class ArticleDetails(DetailMixin, View):
    model = Article
    template_name = 'blog/article_details.html'


class AuthorDetails(AuthorDetailMixin, View):
    model = User
    template_name = 'blog/author_details.html'


class NewTag(LoginRequiredMixin, NewObjectMixin, View):
    form = TagForm  # without brackets ()
    success = 'blog:tags'
    view_name = 'blog:new_tag'
    title = 'Tag'


class NewStartup(LoginRequiredMixin, NewObjectMixin, View):
    form = StartupForm  # without brackets ()
    success = 'blog:startups'
    view_name = 'blog:new_startup'
    title = 'Startup'


class NewArticle(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'text', 'slug', 'author',
              'startup', 'tag', 'published_date']


class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = 'blog/tag_confirm_delete.html'
    context_object_name = 'tag'
    success_url = '/tags/'


class StartupDelete(LoginRequiredMixin, DeleteView):
    model = Startup
    template_name = 'blog/startup_confirm_delete.html'
    context_object_name = 'startup'
    success_url = reverse_lazy('blog:startups')


class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('blog:articles')



class ArticleEdit(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'text', 'slug', 'author',
              'startup', 'tag', 'published_date']


class Search(View):

    def get(self, request):
        get_content = self.request.GET.get('search')

        if not get_content:
            return render(request, 'blog/search_result.html', context={'articles': Article.objects.all()})

        articles = Article.objects.filter(Q(title__contains=get_content) | Q(text__contains=get_content))
        return render(request, 'blog/search_result.html', context={'articles': articles})