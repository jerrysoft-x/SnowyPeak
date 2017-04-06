# lass Student(object):
#
#     def get_score(self):
#          return self._score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
# 现在，对任意的Student实例进行操作，就不能随心所欲地设置score了：
#
# >>> s = Student()
# >>> s.set_score(60) # ok!
# >>> s.get_score()
# 60
# >>> s.set_score(9999)
# Traceback (most recent call last):
#   ...
# ValueError: score must between 0 ~ 100!


class Student(object):
    def get_score(self):
        return self.__score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value <0 or value > 100:
            raise ValueError('score must between 0 and 100!')
        self.__score = value

s = Student()
s.set_score(60)
print(s.get_score())
# s.set_score(9999)
# print(s.get_score())