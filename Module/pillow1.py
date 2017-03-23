from PIL import Image

im = Image.open('IMG_4597.JPG')
print(im.format, im.size, im.mode)
im.thumbnail((800, 600))
im.save('thumb.jpg', 'JPEG')
