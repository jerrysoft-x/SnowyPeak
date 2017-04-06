# >>> def fn(self, name='world'): # 先定义函数
# ...     print('Hello, %s.' % name)
# ...
# >>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
# >>> h = Hello()
# >>> h.hello()
# Hello, world.
# >>> print(type(Hello))
# <class 'type'>
# >>> print(type(h))
# <class '__main__.Hello'>


def fn(self, name = 'world'):
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello = fn))

h = Hello()
h.hello()
print(type(h))