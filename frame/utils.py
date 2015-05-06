import requests
from django.conf import settings
import mimetypes

def upload(file_instance):
    name = file_instance.name
    data = file_instance.read()
    mimetype, encoding = mimetypes.guess_type(name)

    frame_upload_request = requests.post(settings.FRAME_URL, files={'attachment': (name, data, mimetype)})

    if frame_upload_request.status_code == 200:
        return frame_upload_request.content
    else:
        return None
