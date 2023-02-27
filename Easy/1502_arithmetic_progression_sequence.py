"""
Leetcode #1502 - Easy

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive
elements is the same. Given an array of numbers arr, return true if the array can be rearranged to form
an arithmetic progression. Otherwise, return false.
"""


def arithmetic_progression_sequence(arr: list) -> bool:
    """
    This function takes as an input an array of integers and returns a boolean denoting if the numbers
    in the array can create an arithmetic progression, meanning, if the difference between any two
    consecutive numbers is the constant.

    :param arr: array of integers
    :return: True, False

    Example:
        (1) arr = [2, 1, 3]
            arithmetic_progression_sequence(arr) => True

    Spacetime Complexity:   O(1)/O(n), where n is the size of the array,
                            because of temp_set and set(arr) creations.
    """
    if len(arr) < 2:
        return False
    elif len(arr) == 2:
        return True
    d = (max(arr) - min(arr))/(len(arr) - 1)
    if d != int(d):
        return False
    temp_set = set(range(min(arr), max(arr) + 1, int(d)))
    return temp_set == set(arr)


# ----------------- TESTS -----------------

arr1 = [3, 5, 1]
print(arithmetic_progression_sequence(arr1))
# Expected Output: True

arr1 = [2, 4, 1]
print(arithmetic_progression_sequence(arr1))
# Expected Output: False

arr1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(arithmetic_progression_sequence(arr1))
# Expected Output: True

arr1 = [20, 15, 10, 6, 1]
print(arithmetic_progression_sequence(arr1))
# Expected Output: False
