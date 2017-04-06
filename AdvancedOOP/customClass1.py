# >>> class Student(object):
# ...     def __init__(self, name):
# ...         self.name = name
# ...     def __str__(self):
# ...         return 'Student object (name: %s)' % self.name
# ...
# >>> print(Student('Michael'))
# Student object (name: Michael)


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

s = Student('Michael')
print(s)