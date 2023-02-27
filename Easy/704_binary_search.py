"""
Leetcode #704 Easy

Given an array of integers, nums, which is sorted in ascending order, and an integer target, write a function to search
target in nums. If target exists, then return its index. Otherwise, return -1. You must write an algorithm with
O(log n) runtime complexity.
"""


def binary_search_logn(arr: list, target: int) -> int:
    """
    By using the binary search method, it returns the index position of the target if found, else returns -1.

    Example:
        (1)
    """

    beg_index = 0
    last_index = len(arr) - 1
    while beg_index <= last_index:
        median = (beg_index + last_index) // 2
        if arr[median] == target:
            return median
        elif arr[median] < target:
            beg_index = median + 1
        else:
            last_index = median - 1
    return -1


# ----------------- TESTS -----------------

arr_1 = [-1, 0, 3, 5, 9, 12]
target_1 = 9
print(binary_search_logn(arr_1, target_1))
# Expected Output: 4

arr_2 = [-1, 0, 3, 5, 9, 12]
target_2 = 2
print(binary_search_logn(arr_2, target_2))
# Expected Output: -1
