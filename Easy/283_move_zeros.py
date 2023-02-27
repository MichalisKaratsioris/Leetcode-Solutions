"""
Leetcode #283 Easy

Given an integer array nums, move all 0's to the end of it while maintaining the relative 
order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

def move_zeros(nums: list) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    
    for num in nums:
        if num == 0:
            nums.remove(num)
            nums.append(0)
    print(nums)


# ----------------- TESTS -----------------

arr = [0, 1, 0, 3, 12]
move_zeros(arr)
# Expected Output: [1, 3, 12, 0, 0]

arr = [0]
move_zeros(arr)
# Expected Output: [0]



