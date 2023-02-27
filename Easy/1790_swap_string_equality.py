"""
Leetcode #1790 - Easy

You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in
a string (not necessarily different) and swap the characters at these indices. Return true if it is possible to make
both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.
"""


def swap_string_equality(s1: str, s2: str) -> bool:
    """
    This function first checks if the two strings are already equal, in which case it returns True.
    It then iterates through the characters of the two strings and counts the number of mismatches.
    If there are exactly two mismatches, it checks if the characters at these indices can be swapped
    to make the strings equal. If this is the case, the function returns True. Otherwise, it returns False.

    :param :
    :return:

    Example:
        Given the input s1="caa" and s2="aaz", the function would return True because we can swap the second
        character of s1 and s2 to make the strings equal: s1="aaz", s2="aaz".

    Spacetime Complexity:     O(1)/O(n), where n is the size of the strings
    """
    if s1 == s2:
        return True
    if len(s1) != len(s2):
        return False
    count = 0
    index1, index2 = -1, -1
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
            if index1 == -1:
                index1 = i
            else:
                index2 = i
    if count != 2:
        return False
    return s1[index1] == s2[index2] and s1[index2] == s2[index1]


# ----------------- TESTS -----------------

s = "bank"
l = "kanb"
print(swap_string_equality(s, l))
# Expected Output: True

s = "attack"
l = "defend"
print(swap_string_equality(s, l))
# Expected Output: False

s = "kelb"
l = "kelb"
print(swap_string_equality(s, l))
# Expected Output: True

s = "caa"
l = "aaz"
print(swap_string_equality(s, l))
# Expected Output: False

s = "abcd"
l = "dcba"
print(swap_string_equality(s, l))
# Expected Output: False
