#==================================================
#
#   Fibonachi.
#   asymptotics: O(fib(N))
#
#==================================================

def fibonacci(n):
    n -= 1
    if n < 0:
        return [], 0
    elif n == 0:
        return [1], 0

    SUM = 2
    fibo = [1,2] + [0]*(n-1)
    for i in range(2, n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
        if fibo[i] % 2 == 0:
            SUM = SUM + fibo[i]
    return fibo, SUM