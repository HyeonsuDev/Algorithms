#Bottom-Up
def fibonacci(self, n):
    memo = {0:0, 1:1}

    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    
    return memo[n]

#Top-Down with Memo
def fibonacci_memo(self, n):

    memo = {}
    if n in [0, 1]:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    return memo[n]

#With Matrix