from datetime import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# from users.models import Profile


class SignupForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', max_length=255, help_text='Обязательно')
    email = forms.EmailField(max_length=200, help_text='Обязательно')

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')


class UserDataForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'first_name',
            'last_name',
        ]
        labels = {"email": "Email",
                  "first_name": "Имя",
                  "last_name": "Фамилия"
                  }
