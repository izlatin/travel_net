from django import forms

from .models import Publication


class CreatePublicationForm(forms.ModelForm):
    text = forms.CharField(label='Текст', widget=forms.Textarea)

    class Meta:
        model = Publication
        fields = ('location',)
