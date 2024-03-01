from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
