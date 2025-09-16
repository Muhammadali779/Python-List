nums = [1, 2, 3, 7, 8, 9]

sum_10 = []

for i in range(len(nums)):
    for n in range(i+1, len(nums)):
        if nums[i] + nums[n] == 10:
            sum_10.append((nums[i], nums[n]))

print(sum_10)
