"""
Leetcode #1779 - Easy

You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y).
You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi).
A point is valid if it shares the same x-coordinate or the same y-coordinate as your location. Return the index
(0-indexed) of the valid point with the smallest Manhattan distance from your current location. If there are multiple,
return the valid point with the smallest index. If there are no valid points, return -1. The Manhattan distance
between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).

Constraints:
    1 <= points.length <= 104
    points[i].length == 2
    1 <= x, y, ai, bi <= 104

"""


def nearest_point_same_xy(x: int, y: int, arr: list) -> int:
    """
    This function will find the valid point with the smallest Manhattan distance from the current location (x, y).
    If there are no valid points, it will return -1.

    :param arr:
    :return:

    Example:
        (1) x = 3
            y = 4       points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
            nearest_point_same_xy(x, y) => 2

    Spacetime Complexity:     O(1)/O(n), where n is the size of the array
    """
    min_distance = float('inf')
    min_index = -1
    for i, (a, b) in enumerate(arr):
        if a == x or b == y:
            distance = abs(a - x) + abs(b - y)
            if distance < min_distance:
                min_distance = distance
                min_index = i
    return min_index


# ----------------- TESTS -----------------

arr = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]
x = 3
y = 4
print(nearest_point_same_xy(x, y, arr))
# Expected Output: 2

arr = [[3, 4]]
x = 3
y = 4
print(nearest_point_same_xy(x, y, arr))
# Expected Output: 0

arr = [[2, 3]]
x = 3
y = 4
print(nearest_point_same_xy(x, y, arr))
# Expected Output: -1
