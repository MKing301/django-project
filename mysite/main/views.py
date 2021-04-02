from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import NewUserForm, UserChangeForm, EditProfileForm

# Create your views here.
def index(request):
    return render(request=request, template_name="main/index.html")


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("main:index")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    return render(request=request, template_name="registration/register.html", context={"form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("main:index")
            else:
                messages.error(request, "Invalid username and/or password!")

        else:
            messages.error(request, "Invalid username and/or password!")

    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"form":form})


def view_profile(request):
    args = {'user': request.user}
    return render(request=request, template_name='main/profile.html', context=args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, f"Your profile was updated successfully.")
            return redirect('main:view_profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request=request, template_name="main/edit_profile.html", context=args)


def password_change_request(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, f"Your password was updated successfully.")
            return redirect('/profile')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request=request, template_name="accounts/password_change.html", context=args)


def logout_request(request):
    logout(request)
    return redirect("main:index")