import json
d = dict(name='Bob', age=20, score=88)
print(d)
j = json.dumps(d)
print(j)
d2 = json.loads(j)
print(d2)