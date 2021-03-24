from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib import messages


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    messages.success(request, "Logged in successfully!")


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    messages.success(request, "Logged out successfully!")
