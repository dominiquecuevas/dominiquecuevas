def get_max_profit(stock_prices):
    '''
    >>> stock_prices = [10, 7, 5, 8, 11, 9]
    >>> get_max_profit(stock_prices)
    6
    '''

    profit = 0
    for i in range(1, len(stock_prices)):
        if stock_prices[i] - stock_prices[i-1] > 0:
            profit += stock_prices[i] - stock_prices[i-1]
    return profit

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('all tests passed.')