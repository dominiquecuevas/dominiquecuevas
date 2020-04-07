def find_rotational_point(words):
    '''
    >>> words = ['ptolemaic', 'retrograde', 'supplant', 'undulate', 'xenoepist', 'asymptote', 'babka', 'banoffee', 'engender', 'karpatka', 'othellolagkage',]
    >>> find_rotational_point(words)
    5
    >>> words = ['a', 'b', 'c', 'd']
    >>> find_rotational_point(words)
    0
    >>> words = ['b', 'c', 'd', 'e', 'f', 'a']
    >>> find_rotational_point(words)
    5
    >>> words = ['e', 'f', 'a', 'b', 'c', 'd']
    >>> find_rotational_point(words)
    2

    '''

    first_word = words[0]
    floor_idx = 0
    ceiling_idx = len(words) - 1

    while floor_idx < ceiling_idx:
        guess_idx = floor_idx + ((ceiling_idx - floor_idx) // 2)
        if words[guess_idx] >= first_word:
            floor_idx = guess_idx
        else:
            ceiling_idx = guess_idx
        if floor_idx + 1 == ceiling_idx:
            return ceiling_idx
    
    # time complexity is O(log n)
    # space complexity is constant O(1)

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('all tests passed.')