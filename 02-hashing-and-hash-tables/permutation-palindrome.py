def permutation_palindrome(string):
    '''
    return Boolean if any permutation of input is a palindrome
    >>> permutation_palindrome('ivicc')
    True
    >>> permutation_palindrome('lcivi')
    False
    >>> permutation_palindrome('dcrscwsdwrcc')
    True
    '''
    odd_characters = set()
    for char in string:
        if char in odd_characters:
            odd_characters.remove(char)
        else:
            odd_characters.add(char)
    return len(odd_characters) <= 1

    # time complexity O(n) for loop
    # space complexity O(n) for string length
    # OR say O(k) for possible characters in ASCII/Unicode
    # OR say O(1) is constant for a set

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('All tests passed')