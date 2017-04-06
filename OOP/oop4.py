print(len('ABC'))
print('ABC'.__len__())

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))
print(getattr(obj, 'x'))
print(hasattr(obj, 'y'))
print(obj.x)
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)
