class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        elif attr == 'age':
            return lambda: 25
        else:
            # raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
            raise AttributeError(r"'Student' object has no attribute '{}'".format(attr))
s = Student()
print(s.name)
s.score = 60
print(s.score)
print(s.age())
print(s.abc)
