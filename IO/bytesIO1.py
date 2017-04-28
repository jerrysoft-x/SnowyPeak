# >>> from io import BytesIO
# >>> f = BytesIO()
# >>> f.write('中文'.encode('utf-8'))
# 6
# >>> print(f.getvalue())
# b'\xe4\xb8\xad\xe6\x96\x87'

from io import BytesIO
f = BytesIO()
print(f.write('中文'.encode(encoding='utf-8')))
print(f.getvalue())