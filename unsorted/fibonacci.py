import itertools
import functools
import time

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__name__, *args} took {(end - start) * 1_000: .3f} milliseconds')
        print(result)
        return result
    return wrapper

@functools.lru_cache()
@timeit
def fib_r(n):
    if n == 0 or n == 1:
        return 1
    return fib_r(n-1) + fib_r(n-2) 

@timeit
def fib_i(n):
    # if n == 0 or n == 1:
    #     return [0, 1]
    # x = fib_i(n-1)
    # return  x + [x[-2] + x[-1]]
    fibs = []
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        fibs.append(a)
    return fibs

def fib_g(a=1, b=1):
    while True:
        yield a
        a, b = b, a + b

@timeit
def fib_gen(n):
    return [*itertools.islice(fib_g(), n)]

@timeit
def fib_gen_i(n):
    fib_i = iter(fib_g())
    return [next(fib_i) for i in range(n)]

@timeit
def fib_gen_m(m):
    # fibs = []
    # for i in iter(fib_g()):
    #     if i > m:
    #         break
    #     fibs.append(i)
    # return fibs
    # fib_i = iter(fib_g())
    
    # return [i if i <= m else i for i in fib_i]
    g = fib_g()
    return [
        i
        if i <=m
        else g.close()
        for i in iter(g)
    ][:-1]
    # return [i if i <= m else i for i in range(0, m, 10)]



N = 90
# fib_r(N)
# fib_i(N)
# fib_gen(N)
fib_gen_m(N)
# assert fib_gen_m(90) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
