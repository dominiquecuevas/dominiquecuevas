def flight_movie(flight_length, movie_lengths):
    '''
    Write a function that takes an integer flight_length (in minutes) and 
    a list of integers movie_lengths (in minutes) and 
    returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.
    
    test:
    >>> flight_length = 600
    >>> movie_lengths = [100, 200, 300, 300, 400]
    >>> flight_movie(flight_length, movie_lengths)
    True
    >>> flight_length = 600
    >>> movie_lengths = [100, 200, 200, 250, 300]
    >>> flight_movie(flight_length, movie_lengths)
    False

    '''
    seen = set()
    for movie1 in movie_lengths:
        movie2 = flight_length - movie1
        if movie2 in seen:
            return True
        seen.add(movie1)
    
    return False

    # time complexity O(n) for checking each item in movie_lengths; using a set made lookup O(1)
    # space complexity O(n) for the length of the seen set

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('All tests passed')