# 构造从3开始的奇数序列，生成器
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


# 筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0


# 素数生成器
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break

