from django.db.models import Field
from django.db.models import SubfieldBase
from django.conf import settings
from frame.forms import FrameFileField
from frame.utils import upload
import urllib

class FrameImage(object):
    def __init__(self, key):
        self.key = key

    def build_url(self, **kwargs):
        url = '%s/image/%s' % (settings.FRAME_URL, self.key)
        if kwargs:
            options = urllib.urlencode(kwargs)
            url += '?%s' % options
        return url

    @staticmethod
    def from_file(file_instance):
        key = upload(file_instance)
        return FrameImage(key)


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
