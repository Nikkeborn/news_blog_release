from django.test import TestCase


import datetime
from django.utils import timezone
from blog.forms import TagForm, StartupForm


class TagFormTest(TestCase):

    def test_tegform_title_field_label(self):
        form = TagForm()
        self.assertTrue(
            form.fields['title'].label == None or form.fields['title'].label == 'new_test_tag')


class StartupFormTest(TestCase):

    def test_startupform_title_field_label(self):
        form = StartupForm()
        self.assertTrue(
            form.fields['title'].label == None or form.fields['title'].label == 'new_test_startup')


    def test_startupform_title_field_label_equals(self):
        form = StartupForm()
        self.assertEquals(form.fields['title'].label, None)
