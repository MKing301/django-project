from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm, UserChangeForm, EditProfileForm

# Create your views here.
def home(request):
    return render(request=request, template_name="main/home.html")


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"New account created: {username}")
            login(request, user)
            messages.success(request, f"You are now logged in as {username}")
            return redirect("main:home")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    return render(request=request, template_name="main/register.html", context={"form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}")
                return redirect("main:home")
            else:
                messages.error(request, "Invalid username and/or password!")

        else:
            messages.error(request, "Invalid username and/or password!")

    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"form":form})


def view_profile(request):
    args = {'user': request.user}
    return render(request=request, template_name='main/profile.html', context=args)


def logout_request(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("main:home")