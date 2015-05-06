from django.core.files.uploadedfile import UploadedFile
from django.forms.fields import FileField
from django.forms.util import ValidationError as FormValidationError
from frame.utils import upload

class FrameFileField(FileField):
    def clean(self, value, initial):
        value = super(FileField, self).clean(value)
        if isinstance(value, UploadedFile):
            key = upload(value)
            if not key:
                raise FormValidationError('Attach a valid image')
            return key
        else:
            return value


