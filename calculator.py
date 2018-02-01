# print("press key  to  \n1           a*b\n2           a+b\n3           a/b\n4           a-b ")
# k = input()
# a1 = input()
# b1 = input()


def mult(a, b, k):
    if   k == 1:
        q = a * b
    elif k == 2:
        q = a + b
    elif k == 3:
        q = a / b
    else :
        q = a - b
    return q


mult(1, 5, 1)



# def add(a, b):
#     return a + b
#
# def div(a, b):
#     return a / b
#
# def sub(a, b):
#     return a - b
