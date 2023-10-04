def first_missing_positive(nums):
    n = len(nums)

    # Step 1: Rearrange the array to move positive integers to their correct positions
    for i in range(n):
        while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    # Step 2: Find the first index where the value doesn't match its position
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # If all positive integers from 1 to n are present, return n + 1
    return n + 1

# Example usage:
input1 = [3, 4, -1, 1]
input2 = [1, 2, 0]

print(first_missing_positive(input1))  
print(first_missing_positive(input2))  
