import hashlib

md51 = hashlib.md5()
md51.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md51.hexdigest())

md52 = hashlib.md5()
md52.update('how to use md5 in '.encode('utf-8'))
md52.update('python hashlib?'.encode('utf-8'))
print(md52.hexdigest())
