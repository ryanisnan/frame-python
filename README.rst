=====
Frame-python
=====

A helper library to simplify the process of storing and retrieving images from the Frame image server within Python projects. The library can be used in vanilla python, however Form and Model classes are provided for deeper integration with Django

Helper methods
--------------

`frame.models.FrameImage`

A class that simplifies the process of storing and manipulating images in Frame

- `FrameImage(key, frame_url=None)`

A key string must be provided when initializing a FrameImage instance. This is the value that is returned when calling the `upload` method. If `frame_url` is not provided, will attempt to retrieve `frame_url` from Django settings file or from environment variable (set `FRAME_URL` in your environment).

- `frame_image_instance.build_url()`

Returns an absolute url for the image. Optional arguments, such as `width`, `height`, and `quality` may be passed to the method.

- `FrameImage.from_file(file_instance)`

Static method takes a `file` instance and uploads it to frame, then returns an instance for the uploaded image.

`frame.utils.upload(file_instance, frame_url=None)`

Takes a `file` instance and uploads it to frame. Returns a string with the key for the uploaded image. `frame_url` is optional, and follows the same logic as FrameImage to determine the correct value


Integration with Django
-----------------------

1. Add "frame" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'frame',
    )

2. Add a `FRAME_URL` variable to the `settings.py` file with the absolute path to your frame image server::

    FRAME_URL = 'https://my-frame-server.herokuapp.com'

3. Add a `FrameField` field to your models (optional)::

    from frame.models import FrameField
    
    class BlogPost(models.Model):
        title = models.CharField(max_length=120)
        image = FrameField()
