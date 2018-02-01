print("press key  to  \n1           a*b\n2           a+b\n3           a/b\n4           a-b ")
k = int(input())
a = int(input())
b = int(input())


def mult(a1=1, b2=8, k3=2):
    if k3 == 1:
        q = a1 * b2
    elif k3 == 2:
        q = a1 + b2
    elif k3 == 3:
        q = a1 / b2
    else:
        q = a1 - b2
    return q * q


print(mult(a, b, k))

# def add(a, b):
#     return a + b
#
# def div(a, b):
#     return a / b
#
# def sub(a, b):
#     return a - b
