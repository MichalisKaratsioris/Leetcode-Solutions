"""
Given an array of integers nums, calculate the pivot index of this array. The pivot index is the index where the
sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the
index's right. If the index is on the left edge of the array, then the left sum is 0 because there are no elements
to the left. This also applies to the right edge of the array. Return the leftmost pivot index. If no such index exists,
return -1.
"""


def find_pivot_index(arr: list) -> int:
    """
    This function takes as an input
    and returns

    Example:
        (1)
    """

    for i in range(len(arr)):
        if (i == 0) or (i == len(arr) - 1):
            if i == 0:
                l_arr = 0
                r_arr = sum(arr[1:])
                if l_arr == r_arr:
                    return i
            else:
                l_arr = sum(arr[:-1])
                r_arr = 0
                if l_arr == r_arr:
                    return len(arr) - 1
        difference = sum(arr[:i]) - sum(arr[i+1:])
        if difference == 0:
            return i
    return -1


# ----------------- TESTS -----------------

arr_1 = [1, 7, 3, 6, 5, 6]
print(find_pivot_index(arr_1))
# Expected Output: 3

arr_2 = [1, 2, 3]
print(find_pivot_index(arr_2))
# Expected Output: -1

arr_3 = [2, 1, -1]
print(find_pivot_index(arr_3))
# Expected Output: 0
