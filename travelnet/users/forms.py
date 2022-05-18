from datetime import datetime

from django import forms
from django.contrib.auth import get_user_model, forms as auth_forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Profile


class SignupForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', max_length=255, help_text='Обязательно')
    email = forms.EmailField(max_length=200, help_text='Обязательно')

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')


class UserDataForm(forms.ModelForm):

    def clean(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exclude(pk=self.instance.pk):
            raise ValidationError("Пользователь с такой почтой уже сущестсвует")
        return self.cleaned_data

    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'first_name',
            'last_name',
            'image'
        ]
        labels = {
            "email": "Email",
            "first_name": "Имя",
            "last_name": "Фамилия",
            "image": "Аватар"
        }
        # widgets = {
        #     "email": forms.EmailInput(attrs={'readonly': 'readonly'}),
            # "image": forms.ImageField(upload_to='uploads/')
        # }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birthday']
        labels = {'birthday': "Дата рождения"}
        widgets = {'birthday': forms.SelectDateWidget(years=[i for i in range(1901, datetime.now().year)])}


class UserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email")
