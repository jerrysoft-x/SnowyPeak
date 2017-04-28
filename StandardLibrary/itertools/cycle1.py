import itertools, time
cs = itertools.cycle('ABC')
for c in cs:
    print(c)
    time.sleep(1)
