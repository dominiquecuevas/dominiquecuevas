def binary_search(target, nums):
    '''
    >>> target, nums = 5, [0, 1, 2, 3, 4, 5]
    >>> binary_search(target, nums)
    True
    >>> target, nums = 2, [0, 3, 5, 7, 9]
    >>> binary_search(target, nums)
    False
    >>> target, nums = -1, [0, 3, 5, 7, 9]
    >>> binary_search(target, nums)
    False
    >>> target, nums = 0, [0, 3, 5, 7, 9]
    >>> binary_search(target, nums)
    True
    >>> target, nums = 5, [0, 3, 5, 7, 9, 11]
    >>> binary_search(target, nums)
    True
    '''
    # outside bounds of indexes from nums list
    # to be able to move the target to beginning and end indices
    floor_idx = -1
    ceiling_idx = len(nums)

    while floor_idx + 1 < ceiling_idx:
        guess_idx = (ceiling_idx - floor_idx) // 2 + floor_idx
        if nums[guess_idx] == target:
            return True
        if nums[guess_idx] < target:
            floor_idx = guess_idx
        else:
            ceiling_idx = guess_idx
    return False
    # time complexity is O(log n) for cutting the possibilities in half
    # space complexity is O(n)

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('all tests passed')