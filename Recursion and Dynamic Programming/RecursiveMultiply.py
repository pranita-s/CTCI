# TIME - O(log(smallerNumber))


def multiply(m,n):
    if m > n:
        return multiplyHelper(n,m)
    return multiplyHelper(m,n)


def multiplyHelper(m,n):
    if m == 2:
        return n+n
    elif m == 1:
        return n
    halfProduct = multiplyHelper(m/2,n)
    if m % 2:
        return halfProduct+halfProduct+n
    else:
        return halfProduct+halfProduct

print(multiply(7,9))
