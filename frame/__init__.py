import urllib
import os

class FrameImage(object):
    def __init__(self, key, frame_url=None):
        self.key = key
        self.frame_url = frame_url or get_frame_url()

    def build_url(self, **kwargs):
        url = '%s/image/%s' % (self.frame_url, self.key)
        if kwargs:
            options = urllib.urlencode(kwargs)
            url += '?%s' % options
        return url

    @staticmethod
    def from_file(file_instance, frame_url=None):
        from frame.utils import upload
        frame_url = frame_url or get_frame_url()
        key = upload(file_instance, frame_url=frame_url)
        return FrameImage(key, frame_url=frame_url)


def get_frame_url():
    if os.environ.get('FRAME_URL'):
        return os.environ['FRAME_URL']
    else:
        try:
            from django.conf import settings
        except ImportError:
            raise Exception('FRAME_URL could not be retrieved from environment or django settings')
        else:
            return settings.FRAME_URL
