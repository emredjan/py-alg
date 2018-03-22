'''
calculates fibonacci sequence
both naively (recursion) and memoizing (dynamic prog.)
'''

import time
from typing import List, Dict
from test_cases import fib_list


def fib_rec(n: int) -> int:
    '''
    calculates fibonacci sequence naively by recursion
    '''
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)


cache: Dict[int, int] = {}

def fib_dyn(n: int) -> int:
    '''
    calculates fibonacci sequence by memoization
    stores intermediate values in dictionary
    '''
    if n < 2:
        cache[n] = n
        return n

    if (n - 1) in cache.keys():
        if (n - 2) in cache.keys():
            cache[n] = cache[n - 1] + cache[n - 2]
            return cache[n]
        cache[n] = cache[n - 1] + fib_dyn(n - 2)
        return cache[n]

    return fib_dyn(n - 1) + fib_dyn(n - 2)


if __name__ == '__main__':

    # assert and time naive approach
    t0 = time.time()
    for i in range(0, 32):
        assert fib_list[i] == fib_rec(i)
        fib_rec(i)
    t1 = time.time()

    print('fib_rec took:', '{:.8f}'.format(t1 - t0), 'seconds for 32 fibonacci calculations')

    # assert and time dynamic approach
    t0 = time.time()
    for i in range(0, 100):
        assert fib_list[i] == fib_dyn(i)
        fib_dyn(i)
    t1 = time.time()

    print('fib_dyn took:', '{:.8f}'.format(t1 - t0), 'seconds for 100 fibonacci calculations')
