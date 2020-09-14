# 0 1 1 2 3 5 8	13 21 34 55	89 144 233 377 610 987 1597 2584 4181 6765

def fib(number):
    a = 0
    b = 1
    for _ in range(number+1):
        yield a
        a, b = b, a+b


for x in fib(20):
    print(x)
