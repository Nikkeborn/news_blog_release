from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class DetailMixin:
    model = None
    template_name = None

    def get(self, request, pk):
        obj = get_object_or_404(self.model, pk__iexact=pk)
        return render(request, self.template_name, context={self.model.__name__.lower(): obj})


class AuthorDetailMixin:
    model = None
    template_name =None

    def get(self, request, pk):
        user = get_object_or_404(self.model, pk__iexact=pk)
        art_query = user.article_author.get_queryset()
        art_li = list(art_query)
        return render(request, self.template_name, context={self.model.__name__.lower(): user, 'art_li': art_li})



class NewObjectMixin:
    form = None
    template_name = 'blog/object_form.html'
    success = None
    view_name = None
    title = None

    def get(self, request):

        return render(request, self.template_name,
                      context={'object_form': self.form, 'title': self.title,
                               'view_name': reverse_lazy(self.view_name),
                               'back_name': reverse_lazy(self.success)}
                      )

    def post(self, request):
        bound_form = self.form(request.POST)

        if bound_form.is_valid():
            bound_form.save()
            return redirect(reverse_lazy(self.success))

        return render(request, self.template_name,
                      context={'object_form': self.form, 'title': self.title,
                               'view_name': reverse_lazy(self.view_name),
                               'back_name': reverse_lazy(self.success)}
                      )