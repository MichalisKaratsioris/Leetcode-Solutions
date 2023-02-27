"""
Leetcode #1232 - Easy

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
"""


def check_straight_line(arr: list) -> bool:
    """
    This function takes as an input
    and returns

    :param arr:
    :return:

    Example:
        (1) arr = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
            check_straight_line(arr1) => True

    Spacetime Complexity:     O(1)/O(n) where n is the size of arr
    """
    if arr[0][0] == arr[1][0] == 0:
        for coord in arr:
            if coord[0] != 0:
                return False
    tan = (arr[1][1] - arr[0][1])/(arr[1][0] - arr[0][0])
    for i in range(len(arr) - 1):
        if tan != (arr[i+1][1] - arr[i][1])/(arr[i+1][0] - arr[i][0]):
            return False
    return True


# ----------------- TESTS -----------------

arr1 = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
print(check_straight_line(arr1))
# Expected Output: True

arr1 = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
print(check_straight_line(arr1))
# Expected Output: False

arr1 = [[0, 0], [0, 1], [0, -1]]
print(check_straight_line(arr1))
# Expected Output: True
