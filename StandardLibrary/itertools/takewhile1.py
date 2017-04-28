import itertools, time

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
# print(list(ns))
output = [x for x in list(ns) if x % 2 == 0]
print(output)
