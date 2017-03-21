def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    print(fs)
    print(i)
    return fs

print(list(range(1, 4)))

f1, f2, f3 = count()

print(f1)
print(f2)
print(f3)

print(f1())
print(f2())
print(f3())