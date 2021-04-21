from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_active = False
        if commit:
            user.save()
            return user


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("first_name", "last_name", 'password', 'email')

    def save(self, commit=True):
        user = super(EditProfileForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.password = self.cleaned_data['password']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            return user


class ContactForm(forms.Form):
    fullname = forms.CharField(max_length=200)
    contact_email = forms.EmailField()
    contact_subject = forms.CharField(max_length=200)
    contact_message = forms.CharField(widget=forms.Textarea)
