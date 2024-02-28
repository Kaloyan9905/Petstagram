from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.forms import AppUserCreationForm, AppUserLoginForm, ProfileEditForm
from petstagram.accounts.models import Profile

UserModel = get_user_model()


class AppUserRegisterView(views.CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')


class AppUserLoginView(auth_views.LoginView):
    form_class = AppUserLoginForm
    template_name = 'accounts/login-page.html'


class AppUserLogoutView(auth_views.LogoutView):
    pass


class AppUserDetailView(views.DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_likes_count'] = \
            sum(p.like_set.count() for p in self.object.photo_set.all())

        return context


class ProfileEditView(views.UpdateView):
    model = UserModel
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={'pk': self.object.pk}
        )


class AppUserDeleteView(views.DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(self.get_success_url())
