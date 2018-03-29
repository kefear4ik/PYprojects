def dig_pow(n, p):
    a = 0
    b = n
    for x in range(len(str(n))):
        a += (n // (10 ** (len(str(b)) - x - 1))) ** (p + x)
        n = n % (10 ** (len(str(b)) - x - 1))

    if a % b == 0:
        return a // b
    else:
        return -1


print(dig_pow(89, 1))
n = 899
print(tuple(enumerate(str(n))))


def fuun(n, p):
    a = 0
    for i, b in enumerate(str(n)):
        a += pow(str(b), p + i)
    return a / n if a % n == 0 else -1



