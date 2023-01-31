from django.contrib import admin

# Register your models here.
# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import ImageSlider


@admin.register(ImageSlider)
class ImageSliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'captions')
