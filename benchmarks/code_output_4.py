# - Time complexity: O(n)
# - Space complexity: O(n)
def myPow(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / myPow(x, -n)
    if n % 2:
        return x * myPow(x, n - 1)
    return myPow(x * x, n / 2)

# Optimize the space complexity of the above code
#
# - Time complexity: O(n)
# - Space complexity: O(1)
def myPow(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / myPow(x, -n)
    res = 1
    while n > 0:
        if n % 2:
            res *= x
        x *= x
        n //= 2
    return res