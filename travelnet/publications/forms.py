from django import forms

from .models import Publication


class CreatePublicationForm(forms.ModelForm):
    text = forms.CharField(label='Текст', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Сегодня я побывал в пабе на старом арбате..'
    }))

    class Meta:
        model = Publication
        fields = ('location', 'text')
