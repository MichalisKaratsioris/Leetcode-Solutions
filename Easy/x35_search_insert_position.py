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

    if arr[0] > target:
        return 0
    if arr[-1] < target:
        return len(arr)
    if len(arr) == 2 and (not target in arr):
        return 1
    beg_index = 0
    last_index = len(arr) - 1
    while beg_index <= last_index:
        median = (beg_index + last_index) // 2
        if arr[median] == target:
            return median
        elif arr[median] < target:
            beg_index = median + 1
            if beg_index == last_index:
                return last_index + 1
        else:
            last_index = median - 1
            if beg_index == last_index:
                return last_index + 1


# ----------------- TESTS -----------------

arr_1 = [1, 3, 5, 6]
target_1 = 5
print(search_insert_position(arr_1, target_1))
# Expected Output: 2

arr_2 = [1, 3, 5, 6]
target_2 = 2
print(search_insert_position(arr_2, target_2))
# Expected Output: 1

arr_3 = [1, 3, 5, 6]
target_3 = 7
print(search_insert_position(arr_3, target_3))
# Expected Output: 4
