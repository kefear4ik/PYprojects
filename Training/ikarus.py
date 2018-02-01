stroka = 'fresadf'
print('df' in stroka)

nums = [1, 2, 3]
nums.append(4)
print(nums)

print(len(nums))

nums.insert(2, 4)
print(nums)

print(nums.index(2))
print(max(nums))
print(min(nums))
print(nums.count(4))
nums.remove(1)
nums.reverse()
print(nums)

print('\n', list(range(1, 9)))

word = ['hey', 'i', 'am', 'a', 'monster']
def printer(x):
    for i in (range(5)):
        print(x[i]+'!')

printer(word)


