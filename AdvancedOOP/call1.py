class Student(object):
    def __init__(self, name):
        self.__name = name

    def __call__(self):
        print('My name is %s.' % self.__name)

s = Student('Michael')
print(callable(s))
s()