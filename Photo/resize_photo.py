from PIL import Image
from os import listdir

directory = "input"
output = "output"
files = listdir(directory)

def width_resize(files, new_width):
    for name_img in files:
        img = Image.open(directory + "/" + name_img)  # image extension *.png,*.jpg
        ratio = (new_width / float(img.size[0]))
        height = int((float(img.size[1]) * float(ratio)))
        img = img.resize((new_width, height), Image.ANTIALIAS)
        img.save(output + "/new_" + name_img)  # format may what u want ,*.png,*jpg,*.gif

def height_resize(files, new_height):
    for name_img in files:
        img = Image.open(directory + "/" + name_img)
        ratio = (new_height / float(img.size[1]))
        width = int((float(img.size[0]) * float(ratio)))
        img = img.resize((width, new_height), Image.ANTIALIAS)
        img.save(output + "/new_" + name_img)


if str(input("С сохранением пропорций? [y/n]: ")) == 'y':
    if str(input("По чему изменять? [1 - W/ 2 - H]: ")) == "1":
        new_width = int(input("Ширина (px): "))
        width_resize(files, new_width)
    else:
        new_height = int(input("Высота (px): "))
        height_resize(files, new_height)

else:
    new_width = int(input("Ширина (px): "))
    new_height = int(input("Высота (px): "))

    for name_img in files: 
        img = Image.open(directory + "/" + name_img)
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save(output + "/new_" + name_img)
