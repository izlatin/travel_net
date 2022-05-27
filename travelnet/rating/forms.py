from django import forms

from .models import PublicationLike


class CommentForm(forms.ModelForm):
    class Meta:
        model = PublicationLike
        fields = ('text',)
        labels = {
            'text': 'Ваш комментарий'
        }
