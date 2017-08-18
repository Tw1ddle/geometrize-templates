import os
import sys

from PIL import Image

path = "/root/Desktop/python/images/"
dirs = os.listdir( path )

for item in dirs:
    if os.path.isfile(path + item):
        im = Image.open(path+item)
        f, e = os.path.splitext(path+item)
        imResize = im.resize((200,200), Image.ANTIALIAS)
        imResize.save(f + ' resized.jpg', 'JPEG', quality = 90)