def lazy_sum(*args):
    def sum_num():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum_num

f = lazy_sum(1, 2, 3, 4, 5, 6, 7, 8, 9)

print(f)

print(f())
