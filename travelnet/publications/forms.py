from django import forms
from mapbox_location_field.forms import LocationField

from .models import Publication


# allows for custom error message
class BetterLocationFormField(LocationField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages = {'required': 'Пожалуйста, укажите локацию, это обязательно.'}


class CreatePublicationForm(forms.ModelForm):
    text = forms.CharField(label='Текст', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Сегодня я побывал в пабе на старом арбате..'
    }))

    author = forms.HiddenInput()

    file = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'}),
        label='Вложения (можно выбрать несколько фото)', required=False
    )

    location = BetterLocationFormField(error_messages={'required': 'asdfaskldjfhasdlkjflkajsdf'}, map_attrs={
        "placeholder": "Выберите геопозицию на карте", "zoom": 7,
        "language": "ru",
        "center": [37.60024739728942, 55.763870740960954]
    })

    class Meta:
        model = Publication
        fields = ('location', 'text')
        error_messages = {
            'location': {
                'required': ("This writer's name is too long."),
            },
        }
