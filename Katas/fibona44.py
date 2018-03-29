def tribonacci(signature, n):
    for x in range(n - 3):
        signature.append(sum(signature[-3:]))
    return signature[:n]


print(tribonacci([0, 1, 1], 2))
