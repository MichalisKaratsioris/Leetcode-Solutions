"""
Leetcode #202 - Easy

Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process:

    1.  Starting with any positive integer, replace the number by the sum of the squares of its digits.
    2   Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a
        cycle which does not include 1.
    3.  Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
"""


def is_happy_number(n: int) -> bool:
    """
    This function takes as an input an integer and returns True if the provided number is a happy one.

    :param n:
    :return: True, False

    Example:
        (1) n = 19
            is_happy_number(n) => True

    Spacetime Complexity:     O(k)/O(k), where k is the number of times the loop is executed.
        - for n = 19,   k = 4
        - for n = 2,    k = 8
        - for n = 21,   k = 13
        - for n = 45,   k = 16
    """
    check = set()
    while n != 1:
        if n in check:
            return False
        check.add(n)
        n = sum(int(d)**2 for d in str(n))
    return True


# def is_happy_number_length(n: int, check=set()) -> int:
#     if n == 1:
#         return 1
#     if n in check:
#         return 0
#     check.add(n)
#     return 1 + is_happy_number_length(sum(int(digit)**2 for digit in str(n)), check)


# ----------------- TESTS -----------------

k = 19
print(is_happy_number(k))
# print(is_happy_number_length(k))
# Expected Output: True

k = 2
print(is_happy_number(k))
# print(is_happy_number_length(k))
# Expected Output: False
