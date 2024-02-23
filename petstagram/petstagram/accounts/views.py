from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect, get_object_or_404
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


def show_profile_details(request, pk):
    return render(request, template_name='accounts/profile-details-page.html')


class ProfileEditView(views.UpdateView):
    model = UserModel
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_object(self, queryset=None):
        user_instance = get_object_or_404(UserModel, pk=self.kwargs.get('pk'))
        profile_instance, _ = Profile.objects.get_or_create(user=user_instance)
        return profile_instance

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={'pk': self.object.pk}
        )



def delete_profile(request, pk):
    return render(request, template_name='accounts/profile-delete-page.html')
