def merge_lists(my_list, alices_list):
    '''
    We have our lists of orders sorted numerically already, in lists. Write a function to merge our lists of orders into one sorted list.

    For example:

    >>> my_list = [3, 4, 6, 10, 11, 15]
    >>> alices_list = [1, 5, 8, 12, 14, 19]
    >>> merge_lists(my_list, alices_list)
    [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
    '''
    merged_list = (len(my_list) + len(alices_list)) * [None]
    
    my_idx = 0
    al_idx = 0
    mg_idx = 0
    while mg_idx < len(merged_list):
        if (not my_idx >= len(my_list) and 
        (al_idx >= len(alices_list) or 
        my_list[my_idx] < alices_list[al_idx])):
            merged_list[mg_idx] = my_list[my_idx]
            my_idx += 1
        else:
            merged_list[mg_idx] = alices_list[al_idx]
            al_idx += 1
        mg_idx += 1

    return merged_list

# time complexity O(n) for checking each item in both lists
# space complexity O(n) for number of elements in merged list

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('All tests passed.')