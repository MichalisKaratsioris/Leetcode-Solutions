"""
Leetcode #189 Easy

Given an array, rotate the array to the right by k steps, where k is non-negative.
"""


def rotate_array_k(arr: list, k: int) -> list:
    """
    This function takes as an input
    and returns

    Example:
        (1)
    """

    for i in range(k):
        n = arr[-1]
        arr.pop()
        arr.insert(0, n)
    return arr


def leftRotation(arr: list, d: int) -> list:
    return arr[d:] + arr[:d]


def rightRotation(arr: list, d: int) -> list:
    return arr[-d:] + arr[:-d]


# ----------------- TESTS -----------------

arr_1 = [1, 2, 3, 4, 5, 6, 7]
k_1 = 3
print(rotate_array_k(arr_1, k_1))
# Expected Output: [5, 6, 7, 1, 2, 3, 4]

arr_2 = [-1, -100, 3, 99]
k_2 = 2
print(rotate_array_k(arr_2, k_2))
# Expected Output: [3, 99, -1, -100]
