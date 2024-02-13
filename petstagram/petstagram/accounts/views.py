from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.forms import AppUserCreationForm, AppUserLoginForm

UserModel = get_user_model()


class AppUserRegisterView(views.CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')


class AppUserLoginView(auth_views.LoginView):
    form_class = AppUserLoginForm
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('home')


def show_profile_details(request, pk):
    return render(request, template_name='accounts/profile-details-page.html')


def edit_profile(request, pk):
    return render(request, template_name='accounts/profile-edit-page.html')


def delete_profile(request, pk):
    return render(request, template_name='accounts/profile-delete-page.html')
