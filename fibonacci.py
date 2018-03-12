'''
calculates fibonacci sequence
both naively (recursion) and memoizing (dynamic prog.)
'''

def fib_rec(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)

for i in range(1, 15):
    print(fib_rec(i))
