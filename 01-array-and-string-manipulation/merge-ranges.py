def merge_ranges(meetings):
    '''
    Your company built an in-house calendar tool called HiCal. 
    You want to add a feature to see the times in a day when everyone is available.

    To do this, you’ll need to know when any team is having a meeting. 
    In HiCal, a meeting is stored as a tuple ↴ of integers (start_time, end_time). 
    These integers represent the number of 30-minute blocks past 9:00am.

    For example:

    (2, 3)  # Meeting from 10:00 – 10:30 am
    (6, 9)  # Meeting from 12:00 – 1:30 pm

    Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.

    For example, given:
    test: 
        >>> merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        [(0, 1), (3, 8), (9, 12)]

    Do not assume the meetings are in order. 
    The meeting times are coming from multiple teams.

    Write a solution that's efficient even when we can't put a nice upper bound on the numbers representing our time ranges. 
    Here we've simplified our times down to the number of 30-minute slots past 9:00 am. 
    But we want the function to work even for very large numbers, like Unix timestamps. 
    In any case, the spirit of the challenge is to merge meetings where start_time and end_time don't have an upper bound.
    '''

    sorted_meetings = sorted(meetings)
    # [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]

    merged = [sorted_meetings[0]]

    for cur_start, cur_end in sorted_meetings[1:]:
        prev_start, prev_end = merged[-1]

        if prev_end >= cur_start:
            merged[-1] = (prev_start, max(prev_end, cur_end))
        else:
            merged.append((cur_start, cur_end))
    return merged

    # time complexity is O(n log n) from sorting - log n for the number of times n is cut in half,
    # then n for the number of times the list has to be combined
    # space complexity is O(n) for the new list being the same size as the original in the worst case

    # walkthrough test case
        # merged = [(0, 1)]
    # (0, 1) (3, 5)
        # merged = [(0, 1), (3, 5)]
    # (3, 5) (4, 8)
        # merged = [(0, 1), (3, 8)]
    # (3, 8) (9,10)
        # merged = [(0, 1), (3, 8), (9, 10)]
    # (9, 10) (10, 12)
        # merged = [(0, 1), (3, 8), (9, 12)]

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print('all tests passed')

# print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))