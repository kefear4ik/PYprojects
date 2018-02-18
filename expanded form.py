def expanded_form(num):
    c = []
    i=0
    while num != 0:
        if num%10!=0:
            c.append(str((num%10)*10**i))
        num = num // 10
        i+=1
    return "+".join(c[::-1])


print(expanded_form(102))
