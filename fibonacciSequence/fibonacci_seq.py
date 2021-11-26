# First method using recursion O(2^n), not efficient at all

def fib_recursion(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_recursion(n-2) + fib_recursion(n-1)
    return result


# Second method using memoization O(n), more efficient

def fib(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_recursion(n-2) + fib_recursion(n-1)
    return result


def fib_memo(n):
    memo = [None] * (n + 1)
    return fib(n, memo)


# Third method using the bottoms up method, still O(n) but we do not need to worry about a recursion error


def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n + 1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i - 2] + bottom_up[i - 1]
    return bottom_up[n]

print(fib_bottom_up(1000))