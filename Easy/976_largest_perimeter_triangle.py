"""
Leetcode #976 - Easy

Given an integer array nums, return the largest perimeter of a triangle with a non-zero area,
formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

Constraints:
    3 <= nums.length <= 104
    1 <= nums[i] <= 106
"""


def largest_perimeter_triangle(arr: list) -> int:
    """
    This function first sorts the nums array in descending order. It then iterates through the array,
    checking if the triangle inequality holds for each possible combination of three sides. If a triangle
    is found, the function returns the perimeter. If the loop completes without finding a triangle, the
    function returns 0.

    :param arr:
    :return:

    Example:
        (1) arr = [3, 2, 3, 4]
            largest_perimeter_triangle(arr) => 10

    Spacetime Complexity:     O(1)/O(nlogn), where n is the size of the array.
    """
    arr.sort(reverse=True)
    for i in range(len(arr) - 2):
        if arr[i] < arr[i + 1] + arr[i + 2]:
            return arr[i] + arr[i + 1] + arr[i + 2]
    return 0


# ----------------- TESTS -----------------

arr = [2, 2, 1]
print(largest_perimeter_triangle(arr))
# Expected Output: 5

arr = [2, 2, 1, 0]
print(largest_perimeter_triangle(arr))
# Expected Output: 5

arr = [1, 2, 1, 10]
print(largest_perimeter_triangle(arr))
# Expected Output: 0

arr = [3, 6, 2, 3]
print(largest_perimeter_triangle(arr))
# Expected Output: 8

arr = [3, 2, 3, 4]
print(largest_perimeter_triangle(arr))
# Expected Output: 10
