"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView)

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("register/", views.register, name="register"),
    path("profile/", views.view_profile, name="view_profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path(
        "accounts/password_change/",
        PasswordChangeView.as_view(template_name='accounts/password_change.html'),
        name="password_change"),
    path(
        "accounts/password_change/done",
        PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
        name="password_change_done"),
    path(
        "accounts/password_reset/",
        PasswordResetView.as_view(template_name='accounts/password_reset.html'),
        name='password_reset'),
    path(
        "accounts/password_reset/done/",
        PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),
    path(
        "accounts/reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    path(
        "accounts/reset/done/",
        PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'),
]
