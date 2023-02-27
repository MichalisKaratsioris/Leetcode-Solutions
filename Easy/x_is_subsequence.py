"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise. A subsequence of a string is
a new string that is formed from the original string by deleting some (can be none) of the characters without
disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""


def is_subsequence(s: str, t: str) -> bool:
    """
    This function takes as an input
    and returns

    Example:
        (1)
    """

    index = -1
    for letter in s:
        next_index = index + 1
        index = t.find(letter, next_index)
        if index == -1:
            return False
    return True


# ----------------- TESTS -----------------

s_1 = "abc"
t_1 = "ahbgdc"
print(is_subsequence(s_1, t_1))
# Expected Output: True

s_2 = "axc"
t_2 = "ahbgdc"
print(is_subsequence(s_2, t_2))
# Expected Output: False

s_3 = "acb"
t_3 = "ahbgdc"
print(is_subsequence(s_3, t_3))
# Expected Output: False
