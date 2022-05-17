from django.core.exceptions import ValidationError
from django.db.models.fields.files import FieldFile
from django.utils.translation import ugettext_lazy as _


def validate_photo_or_video(obj: FieldFile):
    # not sure if this works
    extension = obj.name.split('.')[-1]
    if extension not in ('png', 'jpg', 'mp4', 'webm'):
        raise ValidationError(_('Файл который вы передали не является фото/видео. '
                                'Поддерживаемые форматы: png, jpg, mp4, webm.'))
