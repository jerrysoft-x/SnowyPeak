# >>> m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# >>> m
# <_sre.SRE_Match object; span=(0, 9), match='010-12345'>
# >>> m.group(0)
# '010-12345'
# >>> m.group(1)
# '010'
# >>> m.group(2)
# '12345'
import re

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.groups())
print(m.group(0))
print(m.group(1))
print(m.group(2))
# print(m.groups()[1])
