from django.db.models import Field
from django.db.models import SubfieldBase
from frame.forms import FrameFileField
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
        elif value is None:
            return value
        else:
            return FrameImage(value)

    def get_prep_value(self, value):
        return value.key

    def formfield(self, form_class=FrameFileField, **kwargs):
        return form_class(**kwargs)
