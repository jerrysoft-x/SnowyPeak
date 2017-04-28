# >>> from io import BytesIO
# >>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# >>> f.read()
# b'\xe4\xb8\xad\xe6\x96\x87'

from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
b = f.read()
print(b)
print(b.decode())
