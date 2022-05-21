from datetime import datetime

import sorl
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
    remove_photo = forms.BooleanField(label="Удалить фото", required=False, initial=False)
    image = forms.ImageField(label='Аватар', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.widget_type == 'checkbox':
                visible.field.widget.attrs['class'] = 'form-check-control'
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    def clean(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exclude(pk=self.instance.pk):
            raise ValidationError("Пользователь с такой почтой уже сущестсвует")
        return self.cleaned_data

    def save(self, commit=True):
        instance = super(UserDataForm, self).save(commit=False)
        if self.cleaned_data.get('remove_photo'):
            instance.image.delete(save=False)
        if commit:
            instance.save()
        return instance

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


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control col-2 w-auto ms-3'

    class Meta:
        model = Profile
        fields = ['birthday']
        labels = {'birthday': "Дата рождения"}
        widgets = {'birthday': forms.SelectDateWidget(years=[i for i in range(1901, datetime.now().year)])}


class UserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "email")
