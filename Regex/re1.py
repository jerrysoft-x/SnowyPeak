# >>> import re
# >>> re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
# <_sre.SRE_Match object; span=(0, 9), match='010-12345'>
# >>> re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
# >>>

import re
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345678'))
# print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345678'))

if re.match(r'^\d{3}\-\d{3,8}$', '010-12345678'):
    print('OK')
else:
    print('Failed')
