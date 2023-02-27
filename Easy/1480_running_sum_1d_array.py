"""
Leetcode #1480 Easy

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
"""


def running_sum_one_d_array(arr: list) -> list:
    """
    This function takes as an input
    and returns

    Example:
        (1)
    """

    s = 0
    sums = []
    for number in arr:
        s = s + number
        sums.append(s)
    return sums


# ----------------- TESTS -----------------

arr_1 = [1, 2, 3, 4]
print(running_sum_one_d_array(arr_1))
# Expected Output: [1, 3, 6, 10]

arr_2 = [1, 1, 1, 1, 1]
print(running_sum_one_d_array(arr_2))
# Expected Output: [1, 2, 3, 4, 5]

arr_3 = [3, 1, 2, 10, 1]
print(running_sum_one_d_array(arr_3))
# Expected Output: [3, 4, 6, 16, 17]
