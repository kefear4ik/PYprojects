def solution(number):
    i = 0
    j = 0
    while i < number:
        if i % 3 == 0:
            j = j + i

        elif i % 5 == 0:
            j = j + i
        i += 1
    return j


print(solution(10))
