# def count():
#     def f(j):
#         return lambda: j * j
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i))
#     return fs


def count():
    fs = []
    for i in range(1, 4):
        fs.append((lambda x: lambda: x * x)(i))
    return fs

# print(list(range(1, 4)))

f1, f2, f3 = count()

print(f1)
print(f2)
print(f3)

print(f1())
print(f2())
print(f3())