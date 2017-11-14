import os
import sys

from PIL import Image

# This script recursively scans and creates small thumbnail images from the full-sized images in the templates directories
# Note that this is a potentially destructive action. Only run it if you are sure you want to generate all the template thumbnails anew

def enumerate_files_recursive(dir):
    files = []
    for root, directories, filenames in os.walk(dir):
        for filename in filenames:
            files.append(os.path.normpath(os.path.join(root, filename)).replace('\\', '/'))
    return files

def resize_and_save_image(path, width, height):
    try:
        filepath, extension = os.path.splitext(path)
        if extension == '.chai' or extension == '.json':
            return # Skip files we know aren't images
        
        im = Image.open(path)

        if im.format == 'JPEG':
            if im.width <= width and im.height <= height:
                return # Skip images that are already the right format and size (or smaller)

        filepath, extension = os.path.splitext(path)
        size = (width, height)
        im.thumbnail(size, Image.LANCZOS)

        newpath = filepath + '_thumbnail.jpg'
        im.save(newpath, 'JPEG', quality = 90)
        im.close()

        if path != newpath:
             os.remove(path) # Remove old file (e.g. from converting from .png to .jpg)
    except IOError:
        print("IOError for file path " + path)
    except Exception as ex:
        print("Unknown exception for file path " + path)
        print(ex)

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def resize_all_templates():
    script_path = get_script_path()
    template_dir = script_path + "/../templates/"
    file_paths = enumerate_files_recursive(template_dir)
    
    for file_path in file_paths:
        resize_and_save_image(file_path, 180, 180)

resize_all_templates()