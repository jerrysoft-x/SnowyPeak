import itertools, time

ns = itertools.repeat('ABC', 3)
for n in ns:
    print(n)
    time.sleep(1)
