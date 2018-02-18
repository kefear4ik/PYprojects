def add_binary(a, b):
    return "{0:b}".format(a + b)


print(add_binary(1, 5))

print(str("{0:b}".format(37)))

b = 10
c = ""

a = 0
while b != 0:
    c = str(b % 2) + c
    b = b // 2

print("\n", c)


def converti(a2, b2):
    return bin(a2 + b2).replace('0b', '')

print(converti(2,4))