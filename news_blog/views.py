from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from .forms import UserForm


class Login_(LoginView):

    def get_success_url(self):
        user_name = self.request.POST.get('username')
        user_object = User.objects.get(username=user_name)
        user_id = user_object.pk
        return reverse('blog:author_details', kwargs={'pk': user_id})


class UserRegistration(View):
    form = UserForm
    template_name = 'registration/user_form.html'

    def get(self, request):
        return render(request, self.template_name, context={'form': self.form})

    def post(self, request):
        bound_form = self.form(request.POST)

        if bound_form.is_valid():
            new_user = bound_form.save(commit=False)
            user_pass = new_user.password
            new_user.set_password(user_pass)
            new_user.save()
            user_id = new_user.pk

            return redirect(reverse('blog:author_details', kwargs={'pk': user_id}))

        return render(request, self.template_name, context={'form': self.form})