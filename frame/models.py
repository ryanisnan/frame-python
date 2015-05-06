from django.core.files.uploadedfile import UploadedFile
from django.db.models import Field
from django.db.models import SubfieldBase
from django.forms.fields import FileField
from frame import FrameImage

class FrameField(Field):
    __metaclass__ = SubfieldBase

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 255
        return super(FrameField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return 'CharField'
    
    def to_python(self, value):
        if isinstance(value, FrameImage):
            return value
        elif isinstance(value, UploadedFile):
            return value
        elif not value:
            return value
        else:
            return FrameImage(value)

    def pre_save(self, model_instance, add):
        value = super(FrameField, self).pre_save(model_instance, add)
        if isinstance(value, UploadedFile):
            frame_image = FrameImage.from_file(value)
            setattr(self, self.attname, frame_image)
            return frame_image
        else:
            return value

    def get_prep_value(self, value):
        if isinstance(value, FrameImage):
            return value.key
        else:
            return value

    def formfield(self, form_class=FileField, **kwargs):
        return super(FrameField, self).formfield(form_class, **kwargs)
