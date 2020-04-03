def reverse_words(words):
    '''
    >>> words = ['l', 'a', 'n', 'd', 'e', 'd', ' ', 'h', 'a', 's', ' ', 'e', 'a', 'g', 'l', 'e', ' ', 't', 'h', 'e']
    >>> reverse_words(words)
    >>> words
    ['t', 'h', 'e', ' ', 'e', 'a', 'g', 'l', 'e', ' ', 'h', 'a', 's', ' ', 'l', 'a', 'n', 'd', 'e', 'd']
    '''

    def reverse_characters(words, left_i, right_i):
        while left_i < right_i:
            words[left_i], words[right_i] = words[right_i], words[left_i]
            left_i += 1
            right_i -= 1

    reverse_characters(words, left_i=0, right_i=len(words)-1)
    # ['e', 'h', 't', ' ', 'e', 'l', 'g', 'a', 'e', ' ', 's', 'a', 'h', ' ', 'd', 'e', 'd', 'n', 'a', 'l']

    beg_i = 0
    end_i = 1
    while end_i < len(words):
        if end_i == len(words)-1 or words[end_i+1] == ' ':
            reverse_characters(words, left_i=beg_i, right_i=end_i)
            beg_i = end_i+2
            end_i = beg_i+1
        else:
            end_i += 1

    # time complexity O(n) for checking each element in input
    # space complexity O(1) for fixed # of variables, no new list since mutating in place

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('All tests passed.')