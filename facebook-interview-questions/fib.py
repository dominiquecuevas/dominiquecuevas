def fib(n):
    '''
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    '''
    if n == 0 or n == 1:
        return n
    prev_prev = 0
    prev = 1
    for i in range(n-1):
        curr = prev_prev + prev
        prev_prev = prev
        prev = curr
    return curr

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('all tests passed.')