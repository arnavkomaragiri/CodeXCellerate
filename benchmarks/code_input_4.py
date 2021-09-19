def myPow(x, n):
    if n == 0:
        return 1
    return x * myPow(x, n - 1)