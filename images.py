from PIL import Image, ImageFilter

# video 1 and 2 image section

# img = Image.open('./Pokedex/pikachu.jpeg')


# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img = img.convert('L')

# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)

# filtered_img = img.show()
# crooked = filtered_img.rotate(90)
# resize = filtered_img.resize((300, 300))

# print(img.format)
# print(img.size)
# print(img.mode)
# print(dir(img))

# filtered_img.save("grey.png", 'png')

# crooked.save('crooked.png', 'png')
# resize.save('resize.png', 'png')

# region.save('croped.png', 'png')

# video 3 image section

img = Image.open('astro.jpeg')
print(img.size)

# new_img = img.resize((400, 400))
img.thumbnail((400, 400))
img.save('thumbnail2.jpeg')
