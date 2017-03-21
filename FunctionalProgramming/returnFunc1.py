def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

print(calc_sum(1, 2, 3, 4, 5, 6, 7, 8, 9))
