nums = []
for i in range(3):
    nums.append(input("Enter a number: "))

nums.sort()
print(*nums, sep=', ')


