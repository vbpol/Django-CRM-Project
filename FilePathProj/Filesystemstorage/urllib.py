import mimetypes
import glob, urllib

for file in glob.glob("C:\\Users\\joey\\Desktop\\school\\ICOMMH"):
    url = urllib.pathname2url(file)
    print(file, mimetypes.guess_type(url))