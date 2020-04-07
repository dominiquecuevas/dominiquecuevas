def merge_sorted_nums(my_list, alices_list):
    '''
    >>> my_list     = [3, 4, 6, 10, 11, 15, 21, 33]
    >>> alices_list = [1, 5, 8, 12, 14, 19]
    >>> merge_sorted_nums(my_list, alices_list)
    [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19, 21, 33]
    '''

    merged_list = [None] * (len(my_list) + len(alices_list))

    my_idx = 0
    alices_idx = 0
    for idx in range(len(merged_list)):
        if my_idx < len(my_list) and (alices_idx >= len(alices_list) or my_list[my_idx] < alices_list[alices_idx]):
            merged_list[idx] = my_list[my_idx]
            my_idx += 1
        else:
            merged_list[idx] = alices_list[alices_idx]
            alices_idx += 1
    return merged_list

    # time complexity O(n)
    # space complexity O(n)

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('all tests passed.')