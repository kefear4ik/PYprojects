def reverse(word):
    return word[::-1]


print(reverse("Freedom"))


def spin_words(word):
    if len(word) >= 5:
        return word[::-1]
    else:
        return word


def rev(sentense):
    return " ".join(map(spin_words, sentense.split(" ")))


print(rev('sroirraw fre wollef Hey'))


def rever(sentense1):
    return " ".join(x if len(x) < 5 else x[::-1] for x in sentense1.split(' '))
print(rever('Freedom for all the people'))
