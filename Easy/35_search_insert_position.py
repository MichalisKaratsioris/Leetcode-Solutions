"""
Leetcode #35 Easy

Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order. You must write an algorithm with
O(log n) runtime complexity.
"""


def search_insert_position(arr: list, target: int) -> int:
    """
    This function takes as an input
    and returns

    Example:
        (1)
    """

    if arr[0] >= target:
        return 0
    elif arr[-1] < target:
        return len(arr)
    if len(arr) == 2:
        return len(arr) - 1
    beg_index = 0
    last_index = len(arr) - 1
    while beg_index <= last_index:
        median = (beg_index + last_index) // 2
        if arr[median] == target:
            return median
        elif arr[median] < target:
            beg_index = median + 1
            if beg_index == last_index:
                return last_index
        else:
            last_index = median
            if beg_index == last_index:
                return last_index


# ----------------- TESTS -----------------

nums = [1, 3, 5, 6]
t = 5
print(search_insert_position(nums, t))
# Expected Output: 2

nums = [1, 3, 5, 6]
t = 2
print(search_insert_position(nums, t))
# Expected Output: 1

nums = [1, 3, 5, 6]
t = 7
print(search_insert_position(nums, t))
# Expected Output: 4

nums = [1, 3]
t = 3
print(search_insert_position(nums, t))
# Expected Output: 1

nums = [1, 3, 5]
t = 4
print(search_insert_position(nums, t))
# Expected Output: 2

nums = [1, 2, 4, 6, 7]
t = 3
print(search_insert_position(nums, t))
# Expected Output: 2

nums = [3, 5, 7, 9, 10]
t = 8
print(search_insert_position(nums, t))
# Expected Output: 3
