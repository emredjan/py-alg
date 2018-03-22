'''
Data Structures and Algorithms in Python
Chapter 01 Exercises
'''

#R-1.1
def is_multiple(n: int, m: int) -> bool:
    return n % m == 0

#R-1.2
def is_even(k: int) -> bool:
    pass
    


if __name__ == '__main__':
    assert is_multiple(100, 10) == True
    assert is_multiple(15, 4) == False
    assert is_multiple(3, 9) == False
    assert is_multiple(9, 3) == True