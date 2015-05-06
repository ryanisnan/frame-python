import requests
import mimetypes
from frame import get_frame_url

def upload(file_instance, frame_url=None):
    name = file_instance.name
    data = file_instance.read()
    mimetype, encoding = mimetypes.guess_type(name)

    frame_url = frame_url or get_frame_url()

    frame_upload_request = requests.post(frame_url, files={'attachment': (name, data, mimetype)})

    if frame_upload_request.status_code == 200:
        return frame_upload_request.content
    else:
        return None
