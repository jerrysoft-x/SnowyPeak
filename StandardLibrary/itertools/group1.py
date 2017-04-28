import itertools, time

for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
