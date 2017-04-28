# >>> import re
# # 编译:
# >>> re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# # 使用：
# >>> re_telephone.match('010-12345').groups()
# ('010', '12345')
# >>> re_telephone.match('010-8086').groups()
# ('010', '8086')

import re
reTelephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(reTelephone.match('010-12345').groups())
print(reTelephone.match('010-8086').groups())

