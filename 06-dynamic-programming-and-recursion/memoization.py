class Fibber:
    def __init__(self):
        self.memo = {}
    def fib(self, n):
        if n == 0 or n == 1:
            return n
        if n in self.memo:
            return self.memo[n]
        result = self.fib(n-1) + self.fib(n-2)
        self.memo[n] = result
        print('memo:', self.memo)
        return result

fibber = Fibber()
fibber.fib(5)