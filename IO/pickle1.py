import pickle
d = dict(name='Bob', age=20, score=88)
print(d)
print(pickle.dumps(d))
# with open('dump.txt', 'wb') as f:
#     pickle.dump(d, f)
