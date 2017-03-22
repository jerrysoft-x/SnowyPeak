import functools

'''
In this test case, we can also print out something after the function is executed.
'''


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            print('Start executing...')
            result = func(*args, **kw)
            print('End executing...')
            return result
        return wrapper
    return decorator


@log('Execute')
def now():
    print('2017-03-21')

now()
print(now.__name__)