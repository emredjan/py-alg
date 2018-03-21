'''
calculates fibonacci sequence
both naively (recursion) and memoizing (dynamic prog.)
'''

import time
from typing import List, Dict

# list for testing output
fib_list = [
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
    2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418,
    317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465,
    14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296,
    433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976,
    7778742049, 12586269025, 20365011074, 32951280099, 53316291173,
    86267571272, 139583862445, 225851433717, 365435296162, 591286729879,
    956722026041, 1548008755920, 2504730781961, 4052739537881, 6557470319842,
    10610209857723, 17167680177565, 27777890035288, 44945570212853,
    72723460248141, 117669030460994, 190392490709135, 308061521170129,
    498454011879264, 806515533049393, 1304969544928657, 2111485077978050,
    3416454622906707, 5527939700884757, 8944394323791464, 14472334024676221,
    23416728348467685, 37889062373143906, 61305790721611591, 99194853094755497,
    160500643816367088, 259695496911122585, 420196140727489673,
    679891637638612258, 1100087778366101931, 1779979416004714189,
    2880067194370816120, 4660046610375530309, 7540113804746346429,
    12200160415121876738, 19740274219868223167, 31940434634990099905,
    51680708854858323072, 83621143489848422977, 135301852344706746049,
    218922995834555169026
]


def fib_rec(n: int) -> int:
    '''
    calculates fibonacci sequence naively by recursion
    '''
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)


l: Dict[int, int] = {}

def fib_dyn(n: int) -> int:
    '''
    calculates fibonacci sequence by memoizing
    stores intermediate values in dictionary
    '''
    if n < 2:
        l[n] = n
        return n

    if (n - 1) in l.keys():
        if (n - 2) in l.keys():
            l[n] = l[n - 1] + l[n - 2]
            return l[n]
        l[n] = l[n - 1] + fib_dyn(n - 2)
        return l[n]

    return fib_dyn(n - 1) + fib_dyn(n - 2)

# assert and time naive approach
t0 = time.time()
for i in range(0, 30):
    assert fib_list[i] == fib_rec(i)
    fib_rec(i)
t1 = time.time()

print('fib_rec took:', '{:.8f}'.format(t1 - t0), 'seconds')

# assert and time dynamic approach
t0 = time.time()
for i in range(0, 90):
    assert fib_list[i] == fib_dyn(i)
    fib_dyn(i)
t1 = time.time()

print('fib_dyn took:', '{:.8f}'.format(t1 - t0), 'seconds')
