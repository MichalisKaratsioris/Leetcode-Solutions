"""
Leetcode #9 Easy

Given an integer x, return true if x is a palindrome, and false otherwise.
"""


def palindrome_number(n: int) -> bool:
    """
    This funtion takes as an input an integer n and returns if it is a palindrome or not.

    :param n: Integer
    :return: True/False

    Example:
        (1) n = 121
            Expected Output: True
    """
    if str(n)[0] == str(n)[-1]:
        return True
    return False
    # s = str(n)
    # return s == s[::-1]


# ---------- TESTS -----------

n = 121
print(palindrome_number(n))
# Expected Output: True

n = -121
print(palindrome_number(n))
# Expected Output: False

n = 10
print(palindrome_number(n))
# Expected Output: False

n = 1212
print(palindrome_number(n))
# Answer: False

n = 12121
print(palindrome_number(n))
# Answer: True
