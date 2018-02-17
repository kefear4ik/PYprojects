def binary_array_to_number(arr):
    y = len(arr)
    a = 0
    for i in arr:
        y -= 1
        a = a + (i * 2 ** y)
    return a


print(binary_array_to_number([0, 1, 0, 1]))

print(int('1001', 2))


def f(x1):
    return x1 * x1


a1 = [1, 3, 4]

print(list(map(f, a1)))
