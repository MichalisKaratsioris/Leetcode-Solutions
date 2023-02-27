"""
Leetcode #1 Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


def two_sum(arr: list, t: int) -> list:
    """
    This function takes as an input an array of integers (arr) and an integer (target), and returns
    a list of integers. The return list

    :param arr: Array of integers
    :param t: Integer
    :return: List of integers

    Examples:
        (1) arr = [2, 7, 11, 15]
            Expected Output: [0, 1]

        (2) arr = [3, 2, 4]
            Expected Output: [1, 2]

        (3) arr = [3, 3]
            Expected Output: [0, 1]
    """
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == t:
                return [i, j]


# --------- TESTS -----------

nums = [2, 7, 11, 15]
k = 9
print(two_sum(nums, k))
# Expected Output: [0, 1]

nums = [3, 2, 4]
k = 6
print(two_sum(nums, k))
# Expected Output: [1, 2]

nums = [3, 3]
k = 6
print(two_sum(nums, k))
# Expected Output: [0, 1]

nums = [1, 7, 9, 5, 10, 2]
k = 3
print(two_sum(nums, k))
# Expected Output: [0, 5]

nums = [1, 7, 9, 5, 10, 2]
k = 8
print(two_sum(nums, k))
# Expected Output: [0, 1]

nums = [1, 7, 9, 5, 10, 2]
k = 15
print(two_sum(nums, k))
# Expected Output: [3, 4]
