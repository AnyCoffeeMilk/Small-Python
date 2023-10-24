nums = eval(input())

nums_sorted = sorted(nums)

table = {}
for i in nums_sorted:
    table[i] = nums_sorted.count(i)

def getCount(n_sort_num):
    step_count = 0
    for i in table:
        if i == n_sort_num:
            return step_count, table[i]
        step_count += 1
ans = 0
for i, num in enumerate(nums):
    num_sorted = nums_sorted[i]
    if num != num_sorted:
        nums[i] = num_sorted
    
        step_count, num_count = getCount(num_sorted)
        num_range = nums[step_count : step_count + num_count]
        if num in num_range:
            for num_in_range, j in enumerate(num_range):
                if num_sorted == num_in_range:
                    nums[num_count+j] = num
        else:
            for j in range(len(nums)):
                if nums[-(j+1)] == num_sorted:
                    nums[-(j+1)] = num
                    break
        ans += 1

print(ans)