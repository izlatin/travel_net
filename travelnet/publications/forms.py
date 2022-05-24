from django import forms

from .models import Publication


class CreatePublicationForm(forms.ModelForm):
    text = forms.CharField(label='Текст', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Сегодня я побывал в пабе на старом арбате..'
    }))

    author = forms.HiddenInput()

    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'}),
        label='Вложения (можно выбрать несколько файлов)', required=False
    )

    class Meta:
        model = Publication
        fields = ('location', 'text')
