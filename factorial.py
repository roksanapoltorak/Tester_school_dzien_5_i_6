def factorial(n):

    if n < 0:
        raise ValueError('Factorial is defined only for nonnegative numbers.')

    f=1
    zakres = range(1, n + 1)

    for i in zakres:
        f *= i
    return f