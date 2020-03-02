from django import forms
from .models import *


class TagForm(forms.Form):
    title = forms.CharField(max_length=100)
    slug = forms.SlugField(max_length=200)

    def save(self):
        new_tag = Tag.objects.create(
            title=self.cleaned_data.get('title'),
            slug=self.cleaned_data.get('slug'),
        )
        return new_tag

    title.widget.attrs.update({'class': 'form-control'})
    slug.widget.attrs.update({'class': 'form-control'})


class StartupForm(forms.Form):
    title = forms.CharField(max_length=100)
    slug = forms.SlugField(max_length=200)

    def save(self):
        new_startup = Startup.objects.create(
            title=self.cleaned_data.get('title'),
            slug=self.cleaned_data.get('slug'),
        )
        return new_startup

    title.widget.attrs.update({'class': 'form-control'})
    slug.widget.attrs.update({'class': 'form-control'})
