from PIL import Image, ImageFilter
import sys
import os
from os.path import basename
import errno
import pathlib

# using sys module grab first and second given arguments
# based on the second parameter check if exists or not if not create
# loop through pokedex and convert images to png
# saved them to the new folder

def jpeg_to_png(loop_folder, new_folder):
    if '/' in loop_folder and '/' in new_folder:
        loop_folder = loop_folder.replace('/',"")
        new_folder = new_folder.replace("/","")
    try:
        os.makedirs(new_folder)
        for images in os.listdir(loop_folder):
            img_png = Image.open(f'./{loop_folder}/{images}')
            file_path = img_png.filename
            file_path = os.path.splitext(file_path)[0]
            file_name = basename(file_path)
            # img_png.save(f'./{new_folder}{img_png.filename}', 'png')
            img_png.save(f'./{new_folder}/{file_name}.png', 'png')
            print(file_name)
    except OSError as error:
        if error.errno == errno.EEXIST:
            print("your folder already exists, please try")
        else:
            print(error)
                              
if __name__ == '__main__':
    #loop_folder = sys.argv[1]
    #new_folder = sys.argv[2]
    
    loop_folder = "pokedex"
    new_folder = 'new2'
    jpeg_to_png(loop_folder, new_folder)
