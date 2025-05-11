nums = [-1, 0, 1, 2, -1, -4]
nums.sort()  # Step 1: sort the array
result = []

for i in range(len(nums) - 2):
    if i > 0 and nums[i] == nums[i - 1]:
        continue  # Skip duplicate fixed elements
    
    left = i + 1
    right = len(nums) - 1

    while left < right:
        s = nums[i] + nums[left] + nums[right]
        if s == 0:
            triplet = [nums[i], nums[left], nums[right]]
            result.append(triplet)
            # Skip duplicates for left and right
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            left += 1
            right -= 1
        elif s < 0:
            left += 1
        else:
            right -= 1

print("The output is:", result)
