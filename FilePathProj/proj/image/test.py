# https://stackoverflow.com/questions/30654772/python-3-4-2-urlib-no-attribute-pathname2url
import mimetypes

import glob, urllib
def test(request):
    # search all files inside a specific folder
    # *.* means file name with any extension
    dir_path = r'E:\demos\files_demos\account\**\*.*'
    for file in glob.glob(dir_path, recursive=True):
        
        print(file)