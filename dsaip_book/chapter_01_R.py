'''
Data Structures and Algorithms in Python
Chapter 01 Exercises
'''

from typing import List, Tuple, Any

# R-1.1
def is_multiple(n: int, m: int) -> bool:
    return n % m == 0

# R-1.2
def is_even(k: int) -> bool:
    '''
    bitwise 'and' with 1 gives 0 for even numbers
    https://javarevisited.blogspot.nl/2013/04/how-to-check-if-number-is-even-or-odd.html
    '''
    return k & 1 == 0

# R-1.3  
def minmax(data: List[int]) -> Tuple[int, int]:
    
    min = data[0]
    max = data[0]

    for i in data:
        if i < min:
            min = i
        else:
            max = i
    
    return (min, max)

# R-1.4 / 1.5
def sss_n(n: int) -> int:
    return sum([i**2 for i in range(n)])

# R-1.6 / 1.7
def sss_odd_n(n: int) -> int:
    return sum([i**2 for i in range(n) if i % 2 != 0])

# R-1.8
def find_reverse_index(s: str, i: int) -> Tuple[str, int]:
    j = len(s) + i
    assert s[j] == s[i]
    return (s[i], j)

# R-1.9
def range50_80() -> List[int]:
    return list(range(50, 90, 10))

# R-1.10
def range8_8() -> List[int]:
    return list(range(8, -10, -2))

# R-1.11
def powers_of_2() -> List[int]:
    return [2**i for i in range(9)]

# R-1.12
def choice(l: List[Any], seed=42) -> Any:
    import random
    r = random.Random()
    r.seed(seed)

    i = r.randrange(0, len(l))

    return l[i]



if __name__ == '__main__':
    # tests for R-1.1
    assert is_multiple(100, 10) == True
    assert is_multiple(15, 4) == False
    assert is_multiple(3, 9) == False
    assert is_multiple(9, 3) == True

    # tests for R-1.2
    assert is_even(1) == False
    assert is_even(-5) == False
    assert is_even(57) == False
    assert is_even(2) == True
    assert is_even(-8) == True
    assert is_even(98) == True

    # tests for R-1.3
    assert minmax([4, 5, 1, 0, -3, 8]) == (-3, 8)
    assert minmax([0, 1, 2, 3, 4, 5]) == (0, 5)

    # tests for R-1.4 / 1.5
    assert sss_n(3) == 5
    assert sss_n(8) == 140

    # tests for R-1.6 / 1.7
    assert sss_odd_n(3) == 1
    assert sss_odd_n(8) == 84

    # tests for R-1.8
    assert find_reverse_index('internet', -4) == ('r', 4)
    assert find_reverse_index('annihilate', -5) == ('i', 5)

    # tests for R-1.9 / 1.10 / 1.11
    assert range50_80() == [50, 60, 70, 80]
    assert range8_8() == [8, 6, 4, 2, 0, -2, -4, -6, -8]
    assert powers_of_2() == [1, 2, 4, 8, 16, 32, 64, 128, 256]

    # tests for R-1.12
    assert choice(['a', 'c', 'x', 'y', 'b']) == 'a'
    assert choice(['a', 'c', 'x', 'y', 'b'], seed=3) == 'c'