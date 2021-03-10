from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request=request,
                  template_name="main/home.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main:home")
        else:
            # TODO display error messages (just printing for now)
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm
    return render(request=request,
                  template_name="main/register.html",
                  context={"form":form})