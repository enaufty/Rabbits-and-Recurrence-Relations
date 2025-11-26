memo = {}
def fib(n,k):
    if n in memo:
        return memo[n]

    if n <= 1: #fibonacci start
        return n

    memo[n] = fib(n - 1, k) + k * fib(n - 2, k)
    return memo[n]


answer = fib(29, 5)
print(f"Answer : {answer}")
