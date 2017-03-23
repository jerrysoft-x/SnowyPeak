import functools
int2 = functools.partial(int, base=2)

print(int2('101010101'))
print(int2('1101010101'))
