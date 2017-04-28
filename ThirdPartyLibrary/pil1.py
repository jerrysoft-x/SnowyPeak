from PIL import Image

im = Image.open(r'C:\BaiduYunDownload\有用的图片\QQ截图20160128140725_1.jpg')
w, h = im.size
print('Oringal image size: %sx%s' % (w, h))
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
im.save('thumbnail.jpg', 'jpeg')
