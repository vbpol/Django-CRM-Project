from django.db import models
import datetime

from django.core.files.storage import FileSystemStorage

# Create your models here.
class ImageSlider(models.Model):
    fs = FileSystemStorage()
    captions = models.CharField(max_length=250)
    image=models.ImageField(storage=fs,null=True, blank=True)   

    # def __str__(self):
    #     return 

    # def __unicode__(self):
    #     return 

