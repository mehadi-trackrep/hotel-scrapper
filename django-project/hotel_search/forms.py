from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")
    # Optionally add email field if you want login via email
    # email = forms.EmailField(required=False, help_text="Optional")

    class Meta:
        model = User
        fields = ["username", "password"]


class SearchForm(forms.Form):
    city = forms.CharField(label="City", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Enter city name"
    }))