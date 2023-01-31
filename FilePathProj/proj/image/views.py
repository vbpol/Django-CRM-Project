from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import ImageSlider

# Create your views here.
def index(request):
    if request.method == 'POST':
        files=request.FILES('file')
        caption = request.POST.get['caption']
        ImageSlider.objects.create(caption=caption,image=files)
        images=ImageSlider.objects.all()
        fs = FileSystemStorage()
        file_name = fs.save(files.name,files)
        file_url = fs.url(file_name)
    
        print(file_url)
    
    return render(request,'image/index.html',{'images':images})

# https://stackoverflow.com/questions/30654772/python-3-4-2-urlib-no-attribute-pathname2url
import mimetypes

import glob, urllib
def test(request):
    # search all files inside a specific folder
    # *.* means file name with any extension
    dir_path = r'E:\demos\files_demos\account\**\*.*'
    for file in glob.glob(dir_path, recursive=True):
        
        print(file)