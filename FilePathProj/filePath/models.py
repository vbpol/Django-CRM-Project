from django.db import models

# Create your models here.
# import os
# from django.conf import settings

# class Foo(models.Model):

#     # path = os.path.dirname(os.path.dirname(__file__))
#     # path = os.join(path, ’media’)
#     path = settings.FILE_PATH_FIELD_DIRECTORY
#     video = models.FilePathField(path=path)

from django.conf import settings

class Foo(models.Model):
    audio = models.FilePathField(
        path=settings.FILE_PATH_FIELD_DIRECTORY,
        match='*.mp4',
        recursive=True
        )