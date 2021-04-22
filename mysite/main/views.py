from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import NewUserForm, UserChangeForm, EditProfileForm, ContactForm
from .helpers import email_admin


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'

    def form_valid(self, form):
        messages.success(self.request, 'Your password has been changed successfully.')
        return super().form_valid(form)


# Create your views here.
def index(request):
    return render(request=request, template_name="main/index.html")


def login_request(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active == True:
                        login(request, user)
                        return redirect("main:index")
                    else:
                        messages.error(request, "Please contact Administrator!")
                        return redirect("main:index")

                else:
                    messages.error(request, "Invalid username and/or password!")
                    return redirect("main:index")

            else:
                messages.error(request, "Invalid username and/or password!")
                return redirect("main:index")

        else:
            form = AuthenticationForm()
            return render(request=request, template_name="registration/login.html", context={"form":form})
    else:
        messages.info(request, "You are already logged in.  You must log out to log in as another user.")
        return redirect("main:index")


def register(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = NewUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                first_name = form.cleaned_data.get("first_name")
                last_name = form.cleaned_data.get("last_name")
                username = form.cleaned_data.get("username")
                email = form.cleaned_data.get("email")
                password = form.cleaned_data.get("password1")
                messages.success(request, f"New account created: {username}")

                email_admin(
                    'New User Registered',
                    f'''
                    <p>Greetings!</p>
                    <p>The following user registered:</p>
                    <ul>
                    <li><strong>First Name:</strong> {first_name}</li>
                    <li><strong>Last Name:</strong> {last_name}</li>
                    <li><strong>Username:</strong> {username}</li>
                    <li><strong>Email:</strong> {email}</li>
                    </ul>
                    <p>Be sure to activate their account!</p>
                    '''
                )

                messages.info(request, f"An email is being sent to the Admin to activate your account.")
                return redirect("main:index")
            else:
                for msg in form.error_messages:
                    messages.error(request, f"{msg}: {form.error_messages[msg]}")

        form = NewUserForm
        return render(request=request, template_name="registration/register.html", context={"form": form})
    else:
        messages.info(request, "You are already registered.  You must log out to register another user.")
        return redirect("main:index")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data.get("fullname")
            contact_email = form.cleaned_data.get("contact_email")
            contact_subject = form.cleaned_data.get("contact_subject")
            contact_message = form.cleaned_data.get("contact_message")

            email_admin(
                contact_subject,
                f'''
                <p>Message from <strong>{fullname}</strong> [{contact_email}]</p>
                <p>{contact_message}</p>
                '''
            )

            messages.success(request, f"Email sent!  Thank you for contacting us.")
            return redirect("main:index")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = ContactForm
    return render(request=request, template_name="main/contact.html", context={"form": form})


@login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request=request, template_name='main/profile.html', context=args)


@login_required
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


@login_required
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


@login_required
def logout_request(request):
    logout(request)
    return redirect("main:index")