def reverse(letters):
    '''
    Write a function that takes a list of characters and reverses the letters in place.
    >>> letters = ['a', 'b', 'c', 'd', 'e']
    >>> reverse(letters)
    >>> letters
    ['e', 'd', 'c', 'b', 'a']

    >>> stuff = ['a', 'b']
    >>> reverse(stuff)
    >>> stuff
    ['b', 'a']

    >>> words = ['l', 'a', 'n', 'd', 'e', 'd', ' ', 'h', 'a', 's', ' ', 'e', 'a', 'g', 'l', 'e', ' ', 't', 'h', 'e']
    >>> reverse(words)
    >>> words
    ['e', 'h', 't', ' ', 'e', 'l', 'g', 'a', 'e', ' ', 's', 'a', 'h', ' ', 'd', 'e', 'd', 'n', 'a', 'l']

    '''
    for i in range(len(letters)//2):
        letters[i], letters[-(i+1)] = letters[-(i+1)], letters[i]
    
    # time complexity is O(n); is O(n/2) but drop the 1/2 constant
    # space complexity is O(1) 
    

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('All tests passed.')