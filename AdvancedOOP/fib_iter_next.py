class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            print('start:', start)
            stop = n.stop
            print('stop:', stop)
            step = n.step
            print('step:', step)
            if start is None:
                start = 0
            elif start < 0:
                start += 100
            if stop is None:
                stop = 100
            elif stop < 0:
                stop += 100
            if step is None:
                step = 1
            elif step < 0:
                raise ValueError('negative step is not supported here!')
            elif step == 0:
                raise ValueError('slice step cannot be zero')
            a, b = 1, 1
            lst = []
            for x in range(stop):
                if x >= start and (x-start) % step == 0:
                    lst.append(a)
                a, b = b, a + b
            return lst



# print(list(range(100)))

fib = Fib()

# for n in fib:
#     print(n)

# print(fib[100])
# print(fib[8])
# print(fib[3])

print(fib[0:5])
print(fib[:10])
print(fib[-2:-1])
print(fib[::5])