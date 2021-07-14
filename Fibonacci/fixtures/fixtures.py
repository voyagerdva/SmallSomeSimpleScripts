def fixture0Term():
    maxNumber = 0
    fibo = []
    sumEven = 0
    return (maxNumber, fibo, sumEven)

def fixture1Term():
    maxNumber = 1
    fibo = [1]
    sumEven = 0
    return (maxNumber, fibo, sumEven)

def fixture2Term():
    maxNumber = 2
    fibo = [1, 2]
    sumEven = 2
    return (maxNumber, fibo, sumEven)

def fixture3Term():
    maxNumber = 3
    fibo = [1, 2, 3]
    sumEven = 2
    return (maxNumber, fibo, sumEven)

def fixture20Terms():
    maxNumber = 20
    fibo = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
    sumEven = 14328
    return (maxNumber, fibo, sumEven)
