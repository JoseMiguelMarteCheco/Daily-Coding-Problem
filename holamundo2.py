def product_except_self(nums):
    # Calculate the product of all elements to the left of each element
    left_products = [1] * len(nums)
    left_product = 1
    for i in range(len(nums)):
        left_products[i] = left_product
        left_product *= nums[i]

    # Calculate the product of all elements to the right of each element
    right_products = [1] * len(nums)
    right_product = 1
    for i in range(len(nums) - 1, -1, -1):
        right_products[i] = right_product
        right_product *= nums[i]

    # Calculate the final result by multiplying the left and right products
    result = [left_products[i] * right_products[i] for i in range(len(nums))]

    return result

input1 = [2, 3, 4, 5, 6]
input2 = [5, 6, 10]

output1 = product_except_self(input1)
output2 = product_except_self(input2)

print(output1)  
print(output2)  

#This problem was asked by Uber.
#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# #For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].