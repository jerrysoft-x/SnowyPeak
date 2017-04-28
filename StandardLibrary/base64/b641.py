import base64

raw = b'binary\x00string'
coded = base64.b64encode(raw)
print(coded)
raw2 = base64.b64decode(coded)
print(raw2)
